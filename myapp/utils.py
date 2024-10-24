# utils.py (Create this file if it doesn't exist)
from django.shortcuts import get_object_or_404
from .models import SchoolYear

def get_current_school_year():
    return get_object_or_404(SchoolYear, is_current=True)
