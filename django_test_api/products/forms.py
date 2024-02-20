from django import forms


class ProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.IntegerField()