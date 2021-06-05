from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from course import forms
import course
from course.forms import CourseForm
from users.models import Student, Instructor as ins, User
from course.models import Course as cs, Enrollment
from video.models import Video
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


# def index(request):
#     dict = {}
#     if request.user.is_authenticated:
#         current_user = request.user
#         user_id = current_user.id
#         user_basic_info = User.objects.get(pk=user_id)
#         try:
#             student_more_info = Student.objects.get(user__pk=user_id)
#         except:
#             instructor_more_info = Instructor.objects.get(user_id=user_id)
#         try:
#             if instructor_more_info.is_instructor:
#                 dict = {'user_basic_info': user_basic_info,
#                         'user_more_info': instructor_more_info}
#         except:
#             dict = {'user_basic_info': user_basic_info,
#                     'user_more_info': student_more_info}

#     return render(request, 'index.html', context=dict)

def home(request):
    context = {'home_page': 'active'}
    return render(request, 'index.html', context)


def about(request):
    context = {'about_page': 'active'}
    return render(request, 'about.html', context)


def donate(request):
    context = {'donate': 'active'}
    return render(request, 'donate.html', context)

    
# def instructor_course(request):
#     if request.user.is_authenticated:
#         current_user = request.user
#         user_id = current_user.id
#         user_basic_info = User.objects.get(pk=user_id)
#         user_more_info = Instructor.objects.get(user__pk=user_id)
    
#     if add.method == 'POST':
#         course_form = CourseForm(data=request.POST)

#         if course_form.is_valid:
#             course_form.save(commit=True)
#             return index(request)

#     dict = {'course_form': course_form, 'user_basic_info': user_basic_info, 'user_more_info': user_more_info}

#     return render(request, 'instructor_course.html', context=dict)


def instructor_course(request, user_id):
    user = User.objects.get(pk=user_id)
    course_form = forms.CourseForm()
    if request.method == 'POST':
        course_form = CourseForm(data=request.POST)

        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.instructor = request.user
            course.save()
            return HttpResponseRedirect(reverse('course:course_home'))
    else:
             
        dict = {'course_form': course_form}
        return render(request, 'instructor_course.html', context=dict)


def my_courses(request, user_id):
    course_list = cs.objects.filter(instructor = user_id)

    ins_details = User.objects.get(pk = user_id)
    
    diction = {'title': 'List of Courses', 'course_list': course_list,'ins_details': ins_details}
    return render(request, 'my_courses.html', context=diction)


def course_list(request):
    course_list = cs.objects.all()
    diction = {'title': 'List of Courses','course_list': course_list}
    return render(request, 'course_list.html', context=diction)


def student_my_courses(request, user_id):
    selected = Enrollment.objects.filter(student = user_id)
    course_pk =[]
    for x in selected:
        y = x.encourse
        course_pk.append(y.id)

    course_list = cs.objects.filter(pk__in = course_pk)
    print(course_list)
    print(user_id)
    diction = {'title': 'List of Courses', 'course_list': course_list}
    return render(request, 'student_my_courses.html', context=diction)


def courses_single(request, course_id):
    if request.user.is_authenticated:
        field = 'instructor'
        cour = cs.objects.get(pk = course_id)
        
        field_value = getattr(cour, field)
        us = cour.instructor
        instr = User.objects.get(pk = us.id)

        enrollment = Enrollment.objects.filter(encourse = course_id , student = request.user.id).first()
        all_video = Video.objects.filter(Course = course_id)
        diction = {'course': cour, 'instructor': instr,'enrollment': enrollment, "all": all_video}
        return render(request, 'courses_single.html', context=diction)
    else:
        messages.success(request, 'You are not Registered !! Register NOW!')
        return HttpResponseRedirect(reverse('users:user_register'))


@login_required
def course_enroll(request,course_id):
    
    if request.method == 'POST':
        
        
        current_student = User.objects.get(pk = request.user.id)
        cour = cs.objects.get(pk=course_id)
        
        if( cour != 0):
        
            Enrollment.objects.create(encourse= cour, student = current_student, status= 1)
        
            
            messages.success(request, 'You have enrolled the Course.')
        else:
            messages.error(request)

    return HttpResponseRedirect(reverse('course:course_home'))


def course_dismiss(request, course_id):
    if request.method == 'POST':
        current_student = User.objects.get(pk=request.user.id)
        cour = cs.objects.get(pk=course_id)

        Enrollment.objects.filter(encourse=course_id, student=request.user.id, status = 1).delete()
        
        messages.success(request, 'You have Unenrolled the Course.')
        return HttpResponseRedirect(reverse('course:course_home'))
    else:
        messages.error(request)

