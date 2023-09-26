from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "school"]

class SchoolFilterForm(forms.Form):
    school = forms.CharField(label="Filter by school name", max_length=255)

def hello_world(request, query_string=None):
    newStudent = Student()
    form = StudentForm(instance=newStudent)
    students = Student.objects.all()
    f = StudentForm(request.POST)
    if f.is_valid():
        newStudent = f.save()

    filterForm = SchoolFilterForm()
    filterFormSubmitted = SchoolFilterForm(request.GET)
    if filterFormSubmitted.is_valid():
        query_string_form = filterFormSubmitted.cleaned_data['school']
        students = Student.objects.filter(school=query_string_form)

    context = {
        'students': students,
        'form': form,
        'query_string': query_string,
        'filterForm': filterForm
    }
    return render(request, "index.html", context)

def show_student(request, student_id):
    # student = Student.objects.filter(id=student_id)
    student = Student.objects.get(id=student_id)
    context = {
        'student': student
    }
    return render(request, "studentProfile.html", context)


def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    form = StudentForm(instance=student)
    context = {
        'student': student
    }
    return render(request, "studentProfile.html", context)