from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def candidates(request):
    return render(request, 'candidates.html')

def result(request):
    return render(request, 'result.html')