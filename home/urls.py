from django.urls import path
from .views import homepage, course_detail, students, enroll_now
urlpatterns = [
    path('', homepage, name='homepage'),
    path('course-detail/<course_id>', course_detail, name='course-detail'),
    path('students', students, name='students'),
    path('enroll', enroll_now, name='enroll'),
]