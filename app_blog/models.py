from django.db import models
from users.models import Student, Instructor,User
# from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):

    instructor = models.ForeignKey('users.User', db_column='author',  on_delete=models.CASCADE,related_name='post_author')
    blog_title = models.CharField(max_length=300,verbose_name="Put a Title")
    slug = models.SlugField(max_length=300,unique= True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.blog_title
