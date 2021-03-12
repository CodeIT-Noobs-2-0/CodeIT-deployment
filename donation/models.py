from django.db import models
from account.models import Donor

# Create your models here.

class DonationItem(models.Model):
    item_name = models.CharField(verbose_name='Item Name', max_length=255)
    item_type = models.CharField(verbose_name='Item Type', max_length=255)
    quantity_required = models.IntegerField(verbose_name='Quantity Required', default=1)
    def __str__(self):
        return self.item_name + " ( " + self.item_type + " ) "

class Donated(models.Model):
    donated_by = models.ForeignKey(Donor, on_delete=models.CASCADE, parent_link=True)
    donated_item = models.ForeignKey(DonationItem, on_delete=models.CASCADE)
    donated_on = models.DateTimeField(auto_now_add=True)
    donated_quantity = models.IntegerField(verbose_name='Quantity Donated')
    def __str__(self):
        return str(self.donated_item) + " By " + str(self.donated_by)