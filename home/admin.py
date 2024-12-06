from django.contrib import admin
from .models import Department, Dealers,Booking 
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','c_name','c_phone','c_email','deal_name','booking_date','booked_on')

admin.site.register(Department)
admin.site.register(Dealers)
admin.site.register(Booking, BookingAdmin)