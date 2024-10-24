from django.db import models
from django.contrib.auth.models import User

class StatusChoice(models.TextChoices):
    RENTED = "rented"
    AVAILABLE = "available"
    LOST = "lost"

class SchoolYear(models.Model):
    year = models.CharField(max_length=9, unique=True)  # e.g., "2023/2024"
    is_current = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_current:
            # If this school year is marked as current, unset others
            SchoolYear.objects.filter(is_current=True).update(is_current=False)
        super(SchoolYear, self).save(*args, **kwargs)

    def __str__(self):
        return self.year

class Person(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    birth_date = models.DateField(auto_now=False)
    birth_place = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        abstract = True

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, default=0
    )
    category = models.CharField(max_length=100)
    class_number = models.CharField(max_length=100, blank=True, null=True)
    entry_date = models.DateField(auto_now=False, blank=True, null=True)
    published_date = models.DateField(auto_now=False, blank=True, null=True)
    statu = models.CharField(
        max_length=200, choices=StatusChoice.choices, null=False, blank=False
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Student(Person):
    class_num = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.class_num}"

class RentBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    isReturned = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

class Archive(Person):
    class_name = models.CharField(max_length=200, blank=False, null=False)
    document_name = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.document_name} - {self.class_name}"

class LibraryCard(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    collegeYear = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"Library Card - {self.student_id}"
