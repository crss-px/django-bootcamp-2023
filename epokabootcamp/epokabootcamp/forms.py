from .models import Student
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "school"]

class SchoolFilterForm(forms.Form):
    school = forms.CharField(label="Filter by school name", max_length=255, required=False)
