from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .utils import get_current_school_year

@api_view(['GET'])
def get_school_years(request):
    school_years = SchoolYear.objects.all()
    serializer = SchoolYearSerializer(school_years, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_school_year(request):
    serializer = SchoolYearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_school_year(request, pk):
    try:
        school_year = SchoolYear.objects.get(pk=pk)
    except SchoolYear.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SchoolYearSerializer(school_year, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_school_year(request, pk):
    try:
        school_year = SchoolYear.objects.get(pk=pk)
    except SchoolYear.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    school_year.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_book(request):
    data = request.data
    serializer = BookSerializer(data=data)

    if serializer.is_valid():
        new_book = Book.objects.create(**data, user=request.user)
        result = BookSerializer(new_book, many=False)
        return Response({"New_Book": result.data})
    else:
        return Response(serializer.errors)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBook(request):
    book = Book.objects.filter(user=request.user).order_by("id")
    serializer_book = BookSerializer(book, many=True)
    return Response({"Books": serializer_book.data})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBookByID(request, pk):
    book = get_object_or_404(Book, id=pk)
    serialzer = BookSerializer(book, many=False)
    return Response({"Book": serialzer.data})

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if book.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this book!"},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = BookSerializer(book, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"book": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if book.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this book!"},
            status=status.HTTP_403_FORBIDDEN,
        )

    book.delete()
    return Response(
        {"details": "Delete Book Successfully!!"}, status=status.HTTP_200_OK
    )

# Student views

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_student(request):
    data = request.data.copy()  # Make a mutable copy of the request data
    current_school_year = get_current_school_year()
    serializer = StudentSerializer(data=data)

    if serializer.is_valid():
        new_student = Student.objects.create(
            **data,
            user=request.user,
            school_year=current_school_year
        )
        result = StudentSerializer(new_student, many=False)
        return Response({"New_Student": result.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStudent(request):
    # Retrieve the current school year
    current_school_year = get_object_or_404(SchoolYear, is_current=True)

    # Filter students by user and current school year
    students = Student.objects.filter(user=request.user, school_year=current_school_year).order_by("id")

    serializer_student = StudentSerializer(students, many=True)
    return Response({"Students": serializer_student.data})

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if student.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this student!"},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"student": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    if student.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this student!"},
            status=status.HTTP_403_FORBIDDEN,
        )

    student.delete()
    return Response(
        {"details": "Delete Student Successfully!!"}, status=status.HTTP_200_OK
    )

# RentBook views
# views.py
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rentBook(request):
    data = request.data.copy()
    serializer = RentSerializer(data=data)

    if serializer.is_valid():
        book = get_object_or_404(Book, id=data['book_id'])
        student = get_object_or_404(Student, id=data['student_id'])
        current_school_year = get_current_school_year()

        rentBook = RentBook.objects.create(
            book_id=book,
            student_id=student,
            rent_date=data['rent_date'],
            return_date=data['return_date'],
            isReturned=data.get('isReturned', False),
            user=request.user,
            school_year=current_school_year
        )
        result = RentSerializer(rentBook, many=False)
        return Response({"RentBook": result.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getRentBook(request):
    # Retrieve the current school year
    current_school_year = get_object_or_404(SchoolYear, is_current=True)

    # Filter RentBooks by user and current school year
    rented_books = RentBook.objects.filter(user=request.user, school_year=current_school_year).order_by("id")

    serializer_rent = RentSerializer(rented_books, many=True)
    return Response({"Rented": serializer_rent.data})


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_rentedBooks(request, pk):
    rent = get_object_or_404(RentBook, id=pk)

    if rent.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this rented model!"},
            status=status.HTTP_403_FORBIDDEN,
        )

    serializer = RentSerializer(rent, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"updatedloan": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_rentedBook(request, pk):
    rent = get_object_or_404(RentBook, id=pk)

    if rent.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this rented book!"},
            status=status.HTTP_403_FORBIDDEN,
        )

    rent.delete()
    return Response(
        {"details": "Delete rented book Successfully!!"}, status=status.HTTP_200_OK
    )




# create new archive model
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_archive(request):
    data = request.data
    serializer = ArchiveSerializer(data=data)

    if serializer.is_valid():
        new = Archive.objects.create(**data, user=request.user)
        result = ArchiveSerializer(new, many=False)
        return Response({"Archive": result.data})
    else:
        return Response(serializer.errors)


# get archive from database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getArchive(request):
    archive = Archive.objects.filter(user=request.user).order_by("id")
    serilizer_archive = ArchiveSerializer(archive, many=True)
    return Response({"Archive": serilizer_archive.data})


# updating archive data
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_archive(request, pk):
    archive = get_object_or_404(Archive, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if archive.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this archive model!"},
            status=status.Http_403_FORBIDEN,
        )

    archive.first_name = request.data["first_name"]
    archive.last_name = request.data["last_name"]
    archive.birth_date = request.data["birth_date"]
    archive.birth_place = request.data["birth_place"]
    archive.class_name = request.data["class_name"]
    archive.document_name = request.data["document_name"]

    archive.save()
    serializer = ArchiveSerializer(archive, many=False)
    return Response({"Archive": serializer.data})


# delete archive model
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_archive(request, pk):
    archive = get_object_or_404(Archive, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if archive.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this archive model!"},
            status=status.Http_403_FORBIDEN,
        )

    archive.delete()
    return Response(
        {"details": "Delete Archive model Successfully!!"}, status=status.HTTP_200_OK
    )



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def libraryCard(request):
    # Use serializer with context to pass request information
    serializer = LibraryCardSerializer(data=request.data)

    if serializer.is_valid():
        library_card = serializer.save(user=request.user, school_year=get_current_school_year())
        result = LibraryCardSerializer(library_card, many=False)
        return Response({"LibraryCard": result.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# get all library cards

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getLibraryCard(request):
    # Retrieve the current school year
    current_school_year = get_object_or_404(SchoolYear, is_current=True)

    # Assuming LibraryCard is linked to Student which is linked to SchoolYear
    library_cards = LibraryCard.objects.filter(user=request.user, school_year=current_school_year).order_by("id")

    serializer_card = LibraryCardSerializer(library_cards, many=True)
    return Response({"LibraryCards": serializer_card.data})

# delete librarycard
@api_view(["delete"])
@permission_classes([IsAuthenticated])
def deleteLibraryCard(request, pk):
    card = get_object_or_404(LibraryCard, id=pk)
    
    if card.user != request.user:
        return Response(
            {"Error": "Sorry you can't make a delete operation, you are not authentificated"},
            status=status.HTTP_403_FORBIDDEN
        )
    card.delete()
    return Response(
        {"Details": "A Library Card has been deleted succesfully"},
        status=status.HTTP_200_OK
    )
    
# delete all library cards
@api_view(["delete"])
@permission_classes([IsAuthenticated])
def deleteAllLibraryCard(request):
    try:
        LibraryCard.objects.all().delete()
        return Response(
            {"Response": "All library Cards have been deleted"},
            status=status.HTTP_200_OK
            )
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
