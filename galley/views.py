from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category, Photo




# Create your views here.
def galley(request):
  categories = Category.objects.all()
  photos= Photo.objects.all()
  context = {'categories':categories ,'photos':photos}
  
  return render(request, 'galley/galley.html', context)


def viewphoto(request, pk):
  return render(request, 'galley/photo.html')


def addphoto(request):
  return render(request, 'galley/add.html')


