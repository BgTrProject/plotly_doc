from django.shortcuts import render,redirect

# Create your views here.
def home(requests):
    return render(requests,'home/welcome.html')


def gesis(requests):
    return render(requests,'home/gesis.html')