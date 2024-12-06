from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('dealers', views.dealers, name='dealers'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='department'),
]