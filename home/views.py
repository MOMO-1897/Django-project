from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views={}
    views['feedbacks']=feedback.objects.all()
    views['services']=Service.objects.all

    return render(request, 'index.html')
def contact(request):

    return render(request, 'contact.html')
def elements(request):

    return render(request, 'elements.html')
def portfolio(request):

    return render(request, 'portfolio.html')
def price(request):

    return render(request, 'price.html')
def services(request):

    return render(request, 'services.html')
def about(request):

    return render(request, 'about.html')

