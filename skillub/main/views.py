from django.shortcuts import render


def index(request):
    return render(request,'main/glav.html')

def profile(request):
    return render(request, 'main/about.html')

def glav(request):
    return render(request, 'main/glav.html')

def sovet(request):
    return render(request, 'main/sovet.html')

def recept(request):
    return render(request, 'main/recept.html')
def login(request):
    return render(request, 'registration/.html')