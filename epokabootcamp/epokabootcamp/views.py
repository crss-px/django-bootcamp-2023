from django.shortcuts import render
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name", "surname", "school"]

def hello_world(request, query_string=None):
    newStudent = Student()
    form = StudentForm(instance=newStudent)
    students = Student.objects.all()
    f = StudentForm(request.POST)
    if f.is_valid():
        newStudent = f.save()
    context = {
        'students': students,
        'form': form,
        'query_string': query_string
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