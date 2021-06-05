
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, ListView,DetailView,View,TemplateView,DeleteView
from django.urls import  reverse,reverse_lazy
from app_blog.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UserForm, StudentInfoForm, InstructorInfoForm
from users.models import Student, Instructor
from django.contrib.auth import get_user_model


User = get_user_model()
import uuid

# Create your views here.
class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'my_blogs.html'
class CreateBlog(LoginRequiredMixin,CreateView,User):

    model = Blog
    template_name = 'create_blog.html'
    fields = ('blog_title','blog_content')
    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.instructor = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        # return HttpResponse("Blog added successfully !!")
        # return HttpResponseRedirect(reverse("course:home"))
        # return HttpResponseRedirect(reverse('index'))
        return HttpResponseRedirect(reverse('course:course_home'))
if User is not Instructor:
    class BlogList(ListView):
        context_object_name = 'blogs'
        model = Blog
        template_name = 'blog_list.html'
        queryset = Blog.objects.order_by('-publish_date')

@login_required
def blog_details(request,slug):
        blog = Blog.objects.get(slug=slug)

        return render(request,'blog_details.html',context={'blog':blog})

class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content')
    template_name = 'edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('app_blog:blog_details', kwargs={'slug':self.object.slug})


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    fields = ('blog_title', 'blog_content')
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('course:course_home')
