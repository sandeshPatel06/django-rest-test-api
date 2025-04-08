from django.contrib import admin
from django.urls import path
from serializer import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.allStudent),  # URL for all students
    path('student/<int:pk>/', views.student_detail),  # URL for a single student
]
