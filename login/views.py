from django.shortcuts import render

def iniciar(request):
    return render(request, 'login/iniciar.html')
