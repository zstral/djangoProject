from django.shortcuts import render

def home(request):
    return render(request, 'core/menuprincipal_wiki.html')

def forum(request):
    return render(request, 'core/forowiki.html')

def signup(request):
    return render(request, 'core/registro_wiki.html')

def login(request):
    return render(request, 'core/inicio_sesion_wiki.html')

def account(request):
    return render(request, 'core/micuentatf.html')