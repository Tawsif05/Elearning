from django.contrib import messages
from django.shortcuts import render
from users.forms import UserForm, StudentInfoForm, InstructorInfoForm
from users.models import Student, Instructor
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


def student_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        student_info_form = StudentInfoForm(data=request.POST)

        if user_form.is_valid() and student_info_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.is_instructor = False
            user.set_password(user.password)
            user.save()

            student_info = student_info_form.save(commit=False)
            student_info.user = user
            student_info.save()
            registered = True
    else:
        user_form = UserForm()
        student_info_form = StudentInfoForm()
    dict = {'user_form': user_form,
            'student_info_form': student_info_form, 'registered': registered}
    if registered == True:
        messages.success(request, 'Successfully Registered !')
    return render(request, 'student_register.html', context=dict)


def instructor_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        instructor_info_form = InstructorInfoForm(data=request.POST)

        if user_form.is_valid() and instructor_info_form.is_valid():
            user = user_form.save(commit=False)
            user.is_instructor = True
            user.is_student = False
            user.set_password(user.password)
            user.save()

            instructor_info = instructor_info_form.save(commit=False)
            instructor_info.user = user
            instructor_info.save()
            registered = True
    else:
        user_form = UserForm()
        instructor_info_form = InstructorInfoForm()
    if registered == True:
        messages.success(request, 'Successfully Registered !')
    dict = {'user_form': user_form,
            'instructor_info_form': instructor_info_form, 'registered': registered}

    return render(request, 'instructor_register.html', context=dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("course:course_home"))

            else:
                return HttpResponse("Account is not active!!")
        else:
            messages.success(request, 'Login Informations are wrong. Try Again!!')
            return HttpResponseRedirect(reverse('users:user_login'))
            
    else:
        return render(request, 'login.html', context={})


def login_page(request):
    return render(request, 'login.html', context={})


def user_register(request):
    context = {'home_page': 'active'}
    return render(request, 'user_register.html', context)


@login_required
def profile(request):
    context = {'home_page': 'active'}
    return render(request, 'profile.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('course:course_home'))





