from django.conf.urls import url
from django.urls import path
from users import views
from django.contrib.auth import views as auth_views
from . import views
app_name = 'users'

urlpatterns = [

    path('student_register/', views.student_register, name='student_register'),
    path('instructor_register/', views.instructor_register,
         name='instructor_register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users_login'),
    # path('login/', views.login_page, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('profile/', views.profile, name='user_profile'),
    # path('teachers/', views.teacher, name='teachers'),
    # path('teachers-single/<int:lecturerId>',
    #      views.teacher_single, name='teachers-single'),
]
