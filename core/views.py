from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'core/dashboard.html', {'title': 'esto es una prueba'})