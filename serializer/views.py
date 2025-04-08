from django.shortcuts import render
from .models import student
from django.http import HttpResponse
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def allStudent(request):  
    students = student.objects.all()  
    serializer = StudentSerializer(students, many=True)  
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def student_detail(request, pk):  
    s = student.objects.get(id=pk)
    serializer = StudentSerializer(s)  
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
