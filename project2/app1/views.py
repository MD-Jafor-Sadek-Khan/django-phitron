from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        contact page
                        <a href="/app2/about/"> about <a> 
                        <a href="/"> home <a> ''')
