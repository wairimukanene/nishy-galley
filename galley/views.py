from django.shortcuts import render
from django.http  import HttpResponse



# Create your views here.
def galley(request):
  return render(request, 'galley/galley.html')


def viewphoto(request, pk):
  return render(request, 'galley/photo.html')


def addphoto(request):
  return render(request, 'galley/add.html')


