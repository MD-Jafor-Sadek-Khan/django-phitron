from django.http import HttpResponse

def home(request):
    return HttpResponse('''
                        hello home
                        <a href="/app1/contact/"> contact <a> 
                        <a href="/app2/about/"> about <a> 
                        ''')