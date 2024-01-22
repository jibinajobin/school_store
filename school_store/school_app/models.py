from django.db import models

# Create your models here.

class Department(models.Model):
    department=models.CharField(max_length=250)
    description=models.TextField()
    def __str__(self):
        return self.department
class Course(models.Model):
    course = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course

class Purpose(models.Model):
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return self.purpose
class Student(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=100,null=True, blank=True)
    gender = models.CharField(max_length=255,null=True, blank=True)
    material = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    purpose = models.ForeignKey(Purpose,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
