from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()

    def __str__(self) -> str:
        return self.dept_name
    
class Dealers(models.Model):
    deal_name = models.CharField(max_length=255)
    deal_spec = models.CharField(max_length=255)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    deal_image = models.ImageField(upload_to='dealers')

    def __str__(self) -> str:
        return 'Mr. ' + self.deal_name + ' - ( ' + self.deal_spec + ')'

class Booking(models.Model):
    c_name = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=10)
    c_email = models.EmailField()
    deal_name = models.ForeignKey(Dealers, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
