from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course
from .forms import StudentForm, SchoolFilterForm, CourseForm

def index(request):
    context = {

    }
    return render(request, 'main-page.html', context)


def students_index(request):
    context = {
        'active_menu': 'students'
    }
    return render(request, 'students/students-index.html', context)

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
        'active_menu': 'students'
    }
    return render(request, 'students/registration-form.html', context)


def students_list(request):
    query_string_form = None
    students = Student.objects.all()
    filterForm = SchoolFilterForm()
    filterFormSubmitted = SchoolFilterForm(request.GET)
    if filterFormSubmitted.is_valid():
        query_string_form = filterFormSubmitted.cleaned_data['school']
        students = Student.objects.filter(school=query_string_form)
        if query_string_form == '':
            students = Student.objects.all()
    context = {
        'students': students,
        'query_string': query_string_form,
        'filterForm': filterForm,
        'active_menu': 'students'
    }
    return render(request, "students/students-list.html", context)

# def show_student(request, student_id):
#     # student = Student.objects.filter(id=student_id)
#     student = Student.objects.get(id=student_id)
#     context = {
#         'student': student
#     }
#     return render(request, "studentProfile.html", context)
#
#
# def edit_student(request, student_id):
#     student = Student.objects.get(id=student_id)
#     form = StudentForm(instance=student)
#     context = {
#         'student': student
#     }
#     return render(request, "studentProfile.html", context)





def courses_index(request):
    context = {
        'active_menu': 'courses'
    }
    return render(request, 'courses/courses-index.html', context)


def new_course(request):
    newCourse = Course()
    form = CourseForm(instance=newCourse)
    submittedForm = CourseForm(request.POST)
    courseSaved = False
    if submittedForm.is_valid():
        newCourse = submittedForm.save()
        courseSaved = True

    context = {
        'form': form,
        'courseSaved': courseSaved,
        'active_menu': 'courses'
    }
    return render(request, 'courses/new-course.html', context)

def course_list(request):
    allCourses = Course.objects.all()
    coursesDict = {}
    for course in allCourses:
        studentsInCourse = len(Student.objects.filter(course=course.id))
        courseData = (course, studentsInCourse)
        coursesDict[course.id] = courseData
    print(coursesDict)
    context = {
        'courses' : allCourses,
        'active_menu': 'courses',
        'coursesWithData': coursesDict
    }

    return render(request, "courses/list.html", context)