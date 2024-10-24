from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ['school_year']


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBook
        fields = "__all__"
        read_only_fields = ['school_year']


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"


class LibraryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCard
        fields = "__all__"
        read_only_fields = ['school_year', 'user']

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = "__all__"
