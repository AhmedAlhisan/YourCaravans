from django.db import models
from django.contrib.auth.models import User
from datetime import date



# Create your models here.

class Caravan (models.Model):
    name = models.CharField(max_length=512)
    feature_image=models.ImageField(upload_to="images/")
    description = models.TextField()
    price = models.IntegerField()
    capacity = models.IntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    carvan_status=models.BooleanField(default=False)
    def __str__(self) :
        return self.name
    
    
   



class Booking(models.Model):
    bookinUser = models.ForeignKey(User,on_delete=models.CASCADE)
    caravan = models.ForeignKey(Caravan, on_delete=models.CASCADE)
    note=models.TextField()
    booking_date = models.DateTimeField()



    @property
    def is_past_due(self):
        return date.today() > self.booking_date.date
    

class ContactUs(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=512)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)    