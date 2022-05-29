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
  photo = Photo.objects.get(id=pk)
  return render(request, 'galley/photo.html', {'photo': photo})


def addphoto(request):
  categories = Category.objects.all()
  if request.method =='POST':
    data = request.POST
    image = request.FILES.get('image')
    
    if data['category'] != 'none':
      category =Category.objects.get(id=data['category'])
    elif data['category_new'] != '':
      category, created = Category.objects.get_or_create(name=data['category_new'])
    else:
      category= None
  
    
    
  
  context = {'categories':categories}
  
  return render(request, 'galley/add.html',context)


