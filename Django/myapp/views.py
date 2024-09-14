from django.shortcuts import render

def home(request):
    return render(request, 'workers/home.html')
