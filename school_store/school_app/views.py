from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .models import Department,Course,Student,Purpose
from django.core.exceptions import ValidationError



from django.http import JsonResponse

User = get_user_model()

# Create your views here.
def index(request):
    departments = Department.objects.all()
    return render(request,"index.html",{'departments': departments})
def order(request):
    departments = Department.objects.all()
    purpose = Purpose.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        material = request.POST.get('Materials')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dept_id = request.POST.get('department')
        course_id = request.POST.get('course')
        purpose_id = request.POST.get('purpose')
        address = request.POST.get('address')

        if (name is None):
            messages.info(request, "Please enter name")
        elif(dept_id==" "):
            messages.info(request, "Please select any department")
        elif (material is None):
            messages.info(request, "Please select material")

        elif Student.objects.filter(phone=phone).exists():
            messages.info(request, "Phone number already exists")
        elif Student.objects.filter(email=email).exists():
            messages.info(request, "Email id already exists")

        else:
            dept1 = Department.objects.get(pk=dept_id)
            course1 = Course.objects.get(pk=course_id)
            purpose1 = Purpose.objects.get(pk=purpose_id)

            student = Student(name=name, dob=dob, age=age,gender=gender,material=material,phone=phone,email=email,department=dept1,course=course1,purpose=purpose1,address=address)

            student.save()
            messages.success(request, "Order Confirmed")
            return redirect('school:success')

    return render(request,"order.html",{'departments': departments,'purpose':purpose})
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login")
            return redirect('school:login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST.get('password1')
        password = request.POST.get('password')

        if password1 == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
            else:

                user = User.objects.create_user(username=username,password=password)

                user.save()
                messages.info(request, "User created")
                return redirect('school:login')
        else:
            messages.info(request,"Password did not match")
    return render(request,"register.html")
def get_courses(request, department_id):
    courses = Course.objects.filter(department=department_id)
    data = [{'id': course.id, 'name': course.course} for course in courses]
    return JsonResponse({'courses': data})
def success(request):
    return render(request, "success.html")
