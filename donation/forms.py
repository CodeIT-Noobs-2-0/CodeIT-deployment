from django import forms
from donation.models import *

class DonationRegisterForm(forms.ModelForm):
    class Meta:
        model = DonationItem
        item_name = forms.CharField(max_length=255, help_text='Item Name' )
        item_type = forms.CharField(max_length=255, help_text='Item Type' )
        quantity_required = forms.IntegerField(help_text='Quantity Required')
        fields = ['item_name', 'item_type', 'quantity_required',]

class DonatedByRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donated
        donated_by = forms.CharField(max_length=255, help_text='Donated By')
        donated_item = forms.CharField(max_length=255, help_text='Donated Item')
        donated_quantity = forms.IntegerField(help_text='Quantity Donated')
        fields = "__all__"
