from django import forms

from users.models import Student, Instructor
from course.models import Course, Enrollment
from django.contrib.auth import get_user_model

User = get_user_model()

class CourseForm(forms.ModelForm):
    

    class Meta():
        model = Course
        fields = ('name', 'course_description')



