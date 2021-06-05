from django.conf.urls import url
from django.urls import path
from app_blog import views

app_name = 'app_blog'

urlpatterns = [

    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('blog_list/',views.BlogList.as_view(), name= 'blog_list'),
    path('details/<slug:slug>',views.blog_details,name='blog_details'),
    path('my_blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit_blog/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
    path('delelte_blog/<pk>/', views.DeleteBlog.as_view(), name='delete_blog'),




]
