from django.contrib import admin
from . models import Department
from . models import Course
from . models import Student
from . models import Purpose
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'description')
    search_fields = ('department',)
admin.site.register(Department,DepartmentAdmin)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'department')
    search_fields = ('course',)
admin.site.register(Course,CourseAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','department','phone','gender')
    search_fields = ('name',)
admin.site.register(Student,StudentAdmin)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ('purpose',)
    search_fields = ('purpose',)
admin.site.register(Purpose,PurposeAdmin)

