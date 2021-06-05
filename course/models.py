from django.db import models
from users.models import Student, Instructor,User



# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey('users.User', db_column='instructor',  on_delete=models.CASCADE)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    encourse = models.ForeignKey('course.Course', db_column='Course',  on_delete=models.CASCADE, )
    student = models.ForeignKey('users.User', db_column='Student',  on_delete=models.CASCADE, )
    status = models.IntegerField(blank=True,null=True)
    
    class Meta:
        managed = True
        db_table = "enrollment"
