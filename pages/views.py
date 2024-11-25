from django.shortcuts import render

def home_ru(request):
    return render(request, 'home_ru.html')

def home_uz(request):
    return render(request, 'home_uz.html')

def home_en(request):
    return render(request, 'home_en.html')
