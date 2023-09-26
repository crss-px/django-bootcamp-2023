from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm, SchoolFilterForm

def index(request):
    context = {

    }
    return render(request, 'main-page.html', context)

def registration_form(request):
    newStudent = Student()
    form = StudentForm(instance=newStudent)
    students = Student.objects.all()
    f = StudentForm(request.POST)
    studentSaved = False
    if f.is_valid():
        newStudent = f.save()
        studentSaved = True

    context = {
        'form': form,
        'studentSaved': studentSaved,
    }
    return render(request, 'registration-form.html', context)


def students_list(request):
    query_string_form = None
    students = Student.objects.all()
    filterForm = SchoolFilterForm()
    filterFormSubmitted = SchoolFilterForm(request.GET)
    if filterFormSubmitted.is_valid():
        query_string_form = filterFormSubmitted.cleaned_data['school']
        students = Student.objects.filter(school=query_string_form)
        if query_string_form is '':
            students = Student.objects.all()
    context = {
        'students': students,
        'query_string': query_string_form,
        'filterForm': filterForm
    }
    return render(request, "students-list.html", context)

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