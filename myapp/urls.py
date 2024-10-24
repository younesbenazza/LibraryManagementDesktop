from django.urls import path
from .views import *

urlpatterns = [
    # all books
    path("books/", getBook, name="book"),
    # book by id
    path("books/<str:pk>", getBookByID, name="book_id"),
    # add book
    path("books/add/", add_book, name="add_book"),
    # update book
    path("books/update/<str:pk>/", update_book, name="update_book"),
    # delete book
    path("books/delete/<str:pk>/", delete_book, name="delete_book"),
    
    
    # get students
    path("students/", getStudent, name="student"),
    # add new student
    path("student/add/", add_student, name="add_student"),
    # update student
    path("student/update/<str:pk>/", update_student, name="update_student"),
    # delete student
    path("student/delete/<str:pk>/", delete_student, name="delete_student"),
    
    
    # get archive
    path("archive/", getArchive, name="archive"),
    # add archive
    path("archive/add/", add_archive, name="add_archive"),
    # update archive
    path("archive/update/<str:pk>/", update_archive, name="update_archive"),
    # delete archive
    path("archive/delete/<str:pk>/", delete_archive, name="delete_archive"),
    
    
    # get rented books
    path("rentedbooks/", getRentBook, name="rented_books"),
    # create a rent book model
    path("rentbook/", rentBook, name="rent_book"),
    # update rented book
    path("rentbook/update/<str:pk>/", update_rentedBooks, name="update_rented_book"),
    # delete rented book
    path("rentbook/delete/<str:pk>/", delete_rentedBook, name="delete_rented_book"),
    
    # create Library card
    path("librarycard/create/", libraryCard, name="library_card"),
    # get library cards
    path("librarycards/", getLibraryCard, name="library_cards"),
    # delete library cards
    path("librarycard/delete/<str:pk>/", deleteLibraryCard, name="delete_library_cards"),

    # delete library cards
    path("librarycards/delete/", deleteAllLibraryCard, name="delete_all_library_cards"),

    path("schoolyears/", get_school_years, name="school_years"),
    path("schoolyear/add/", add_school_year, name="add_school_year"),
    path("schoolyear/update/<str:pk>/", update_school_year, name="update_school_year"),
    path("schoolyear/delete/<str:pk>/", delete_school_year, name="delete_school_year"),

    
]
