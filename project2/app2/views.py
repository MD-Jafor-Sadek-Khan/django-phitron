from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse('''
                        about page
                        <a href="/app1/contact/"> contact <a> 
                        <a href="/"> home <a> ''')
