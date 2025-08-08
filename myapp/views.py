from django.shortcuts import render, redirect


# Create your views here.
def a(request):
    return render(request, 'myapp/a.html')

def b(request):
    return render(request, 'myapp/b.html')

def c(request):
    return render(request, 'myapp/c.html')