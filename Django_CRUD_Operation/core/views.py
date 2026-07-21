from django.shortcuts import render, redirect, get_object_or_404

from core.models import Student

# Create your views here.

def home(request):
    return render(request, 'index.html')


def add_student(request):

    if request.method == "POST":
        Student.objects.create(
            student_id=int(request.POST.get('student_id')),
            full_name=request.POST.get('full_name'),
            department=request.POST.get('department'),
            dob=request.POST.get('dob'),
            gender=request.POST.get('gender'),
            address=request.POST.get('address')
        )

    return render(request, 'add_student.html')


def all_student(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'all_student.html', context)

def delete_student(request, id):
    student = Student.objects.filter(id=id)
    student.delete()
    return redirect('all_student')

def view_student(request, id):
    student = Student.objects.filter(id=id)

    context = {
        'student' : student
    }
    return render (request, 'view_student.html', context)

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.student_id = request.POST.get('student_id')
        student.full_name = request.POST.get('full_name')
        student.department = request.POST.get('department')
        student.dob = request.POST.get('dob')
        student.gender = request.POST.get('gender')
        student.address = request.POST.get('address')

        student.save()

        return redirect('all_student')

    context = {
        "student": student
    }

    return render(request, 'edit_student.html', context)