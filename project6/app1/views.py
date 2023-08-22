from django.shortcuts import render, redirect
from . import models


def home(request):
    student = models.Student.objects.all()
    
    return render(request, 'index.html', {'data': student})


def delete_student(request, roll):
    student = models.Student.objects.get(pk = roll).delete()
    return redirect('home')