from django.db.models.query import QuerySet
from django.shortcuts import render 
from django.core.mail import send_mail
from .models import Category,Photo
from django.http import HttpResponse

def portfolio(request):
    category = request.GET.get('category')
    description =""
    if category == None:
        photos = Photo.objects.all()
        description = ""
    else:    
        photos =Photo.objects.filter(category__name__contains=category)
        ime= Category.objects.get(name = category)
        name = ime.name
        print(name)
        if category == name:
            categories = Category.objects.get(name = category)
            description = (
                 categories.description,
            )
            description = ','.join(str(o) for o in description)

        else:
            print("ERROR NO DESCRIPTION FOUND")
            description = ""
        

    categories = Category.objects.all()
   
    
    return render(request,"portfolio.html",{
       "categories": categories,
       "photos": photos,
       "description": description,
       
 
       })
def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")