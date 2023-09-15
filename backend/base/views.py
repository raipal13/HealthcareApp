from django.shortcuts import render

def landing(request):
    return render(request, 'base/root.html')

def home(request):
    return render(request, 'base/Home.html')



