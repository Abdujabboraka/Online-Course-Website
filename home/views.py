from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .models import Course, Student

# Create your views here.
def homepage(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students
    }
    return render(request, 'homepage.html', context)


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    all_courses = Course.objects.all()
    context = {
        'course': course,
        'all_courses': all_courses
    }
    return render(request, 'course_detail.html', context)


from django.shortcuts import render, redirect
from .models import Student, Course


def enroll_now(request):
    context = {
        'courses': Course.objects.all()
    }

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        selected_courses = request.POST.getlist('courses')  # Get selected courses as a list

        # Create the Student instance first (without courses)
        student = Student.objects.create(first_name=first_name, last_name=last_name, email=email)

        # Assign selected courses to the student's many-to-many relationship
        student.courses.set(selected_courses)  # Use set() for many-to-many field assignment

        student.save()  # Save the student instance

        return redirect('homepage')  # Redirect after successful enrollment

    return render(request, 'enroll.html', context)


def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students.html', context)