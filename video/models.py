from django.db import models
from .validators import file_size
from course.models import Course

# Create your models here.


class Video(models.Model):
    Course = models.ForeignKey('course.Course', db_column='Course',on_delete=models.CASCADE, default= -10)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    

    def __str__(self):
        return self.caption
