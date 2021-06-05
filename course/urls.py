from django.conf.urls import url
from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [

    path('', views.home, name='course_home'),
    path('about/', views.about, name='course-about'),
    path('donate/', views.donate, name='donate'),
    path('instructor_course/<int:user_id>/', views.instructor_course,name='instructor_course'),
    path('my_courses/<int:user_id>/',views.my_courses, name='my_courses'),
    path('student_my_courses/<int:user_id>/', views.student_my_courses, name='student_my_courses'),
    path('course_list/', views.course_list, name='course_list'),
    path('courses_single/<int:course_id>/', views.courses_single, name='courses_single'),
    path('course_enroll/<int:course_id>/',views.course_enroll, name='course_enroll'),
    path('course_dismiss/<int:course_id>/',views.course_dismiss, name='course_dismiss'),

]
