from . import views
from django.urls import path
app_name='school'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('order/',views.order,name='order'),
    path('get_courses/<int:department_id>/', views.get_courses, name='get_courses'),
    path('success/',views.success,name='success'),
    path('register/', views.register, name='register')

]