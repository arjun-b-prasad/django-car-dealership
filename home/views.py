from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Dealers
from .forms import BookingForm
# Create your views here.
def index(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def booking(req):
    if req.method=="POST":
        form = BookingForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req,'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(req,'booking.html', dict_form)
def dealers(req):
    dict_deal = {
        'dealer':Dealers.objects.all()
    }
    return render(req,'dealers.html', dict_deal)
def contact(req):
    return render(req,'contact.html')
def department(req):
    dict_dept = {
        'dept':Department.objects.all()
    }
    return render(req,'department.html',dict_dept)