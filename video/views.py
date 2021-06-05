from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import Video_form
from .models import Video
from course.models import Course
from users.models import Student, Instructor as ins, User
from django.contrib import messages


def videolist(request,user_id):
    form = Video_form(user_id)
    if request.method == "POST":

        form = Video_form(user_id,data=request.POST, files=request.FILES)
        form.fields["Course"].queryset = Course.objects.filter(instructor = user_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Requested Video is uploaded.')
            return HttpResponseRedirect(reverse('course:course_home'))
        else:
            form = Video_form(user_id)
    return render(request, 'video_form.html', {"form": form})



def course_videolist(request,course_id):
    cour = Course.objects.get(pk=course_id)
    all_video = Video.objects.filter(Course=course_id)
    instr = User.objects.get(pk=request.user.id)
    diction = {'course': cour, 'instructor': instr, "all": all_video}

    return render(request, 'course_videolist.html', context=diction)


def video_delete(request, x_id):
    Video.objects.filter(pk = x_id).delete()
    messages.success(request, 'Selected Video is removed')
    return HttpResponseRedirect(reverse('course:course_home'))
