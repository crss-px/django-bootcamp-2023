from .models import Student, Course
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "school", "course"]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "department", "credits", "is_active"]

class SchoolFilterForm(forms.Form):
    school = forms.CharField(label="Filter by school name", max_length=255, required=False)
