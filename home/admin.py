from django.contrib import admin
from .models import Course, Student
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'duration')
    list_display_links = ('name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Student)