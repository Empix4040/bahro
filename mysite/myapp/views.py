from django.shortcuts import render 
from django.core.mail import send_mail
from .models import Category,Photo
from django.http import HttpResponse

def portfolio(request):
    category = request.GET.get('category')
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos =Photo.objects.filter(category__name__contains=category)
        
    categories = Category.objects.all()
     
    
    return render(request,"portfolio.html",{
       "categories": categories,
       "photos": photos,
 
       })
def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")