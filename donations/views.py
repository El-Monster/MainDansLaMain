from django.shortcuts import render

# Create your views here.

# creation de la vue pour page index de dons
def index(request):
    return render(request,'donations/index.html')

def user(request):
    return render(request, 'donations/dashboard.html')