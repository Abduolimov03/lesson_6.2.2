from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')
def drama(request):
    return render(request, 'drama.html')
def fantastika(request):
    return render(request, 'fantastika.html')
def jahon_kinolari(request):
    return render(request, 'jahon_kinolari.html')
def jangari(request):
    return render(request, 'jangari.html')
def komediya(request):
    return render(request, 'komediya.html')
def uzbek_kinolari(request):
    return render(request, 'uzbek_kinolari.html')
