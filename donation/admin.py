from django.contrib import admin
from donation.models import DonationItem, Donated
# Register your models here.

admin.site.register(DonationItem)
admin.site.register(Donated)