from django import forms

from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'c_name' : "Customer Name",
            'c_phone' : "Mobile Number",
            'c_email' : "E-mail",
            'deal_name' : "Dealer Name",
            'booking_date' : "Booking Date",
        }