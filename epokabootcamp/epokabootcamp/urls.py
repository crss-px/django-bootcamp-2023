"""
URL configuration for epokabootcamp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-page"),
    path('students/', views.students_index, name="students-index"),
    path('students/register/', views.registration_form, name="registration_form"),
    path('students/list/', views.students_list, name="students-list"),

    path('courses/', views.courses_index, name="courses-index"),
    path('courses/new/', views.new_course, name="add_course"),
    path('courses/list/', views.course_list, name="course_list"),


    # path('student-profile/<int:student_id>', views.show_student),
    # path('student-edit/<int:student_id>', views.edit_student),
    path('admin/', admin.site.urls),
]
