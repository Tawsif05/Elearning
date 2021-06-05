from django import forms
from django.contrib.auth.models import User
from users.models import Student, Instructor
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class StudentInfoForm(forms.ModelForm):
    Dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),label="Date of Birth")

    class Meta():
        model = Student
        fields = ('Dob', 'gender')



class InstructorInfoForm(forms.ModelForm):
    Dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}),label="Date of Birth")

    class Meta():
        model = Instructor
        fields = ('Dob', 'gender')
