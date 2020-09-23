from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

if request.method == "POST":
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
else:
    form = ProductForm()
    # return redirect ('products_list')