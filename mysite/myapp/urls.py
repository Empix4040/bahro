from django.urls import path
from . import views


urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('contact.html',views.contact,name='contact'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('portfolio.html',views.portfolio,name='portfolio'),
    path('about.html',views.about,name='about'),
    path('about/',views.about,name='about')
]