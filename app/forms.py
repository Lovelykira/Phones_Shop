from django import forms
from django.forms.widgets import Select

from app.models import Product, PhoneModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        CHOICES = PhoneModel.objects.all()
        fields = (
            'name',
            'price',
            'in_stock',
            'p_model'
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'update_name'}),
            'price': forms.TextInput(attrs={'class': 'update_price'}),
            'in_stock': forms.TextInput(attrs={'class': 'update_in_stock'}),
            'p_model': forms.Select(attrs={'class': 'update_model'}),
        }
      #  fields['p_model'] = forms.ModelChoiceField(queryset=PhoneModel.objects.all())
