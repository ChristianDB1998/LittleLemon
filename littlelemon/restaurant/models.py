from django.db import models
import uuid

# Create your models here.
class Menu(models.Model):
    menu_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()


    def __str__(self):
         return f'{self.name}'
    
class Booking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
         return f'{self.title} : {str(self.price)}'