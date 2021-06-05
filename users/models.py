from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Dob = models.DateField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHERS = -1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE,'Female'), (GENDER_OTHERS, 'Others')]
    gender = models.IntegerField(choices=GENDER_CHOICES, default=None)
    

    


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Dob = models.DateField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHERS = -1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE,
                                              'Female'), (GENDER_OTHERS, 'Others')]
    gender = models.IntegerField(choices=GENDER_CHOICES, default=None)
    

    
