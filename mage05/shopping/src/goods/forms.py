#encoding: utf-8


from django import forms
from .models import Goods, ShoppingCar, Order

class GoodsAdminForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.Select, choices=[(0, '上线'), (1, '下线')])
    class Meta:
        model = Goods
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price', 0)
        if price <= 0:
            raise forms.ValidationError('价格不正确')

        return price

    def clean_store(self):
        store = self.cleaned_data.get('store', 0)
        if store < 0:
            raise forms.ValidationError('库存不正确')

        return store


class ShoppingCarForm(forms.ModelForm):
    class Meta:
        model = ShoppingCar
        fields = '__all__'
        exclude = ['user']


class OrderAdminForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.Select, label="状态", \
                                choices=list(Order.STATUS_TEXT.items()))
    class Meta:
        model = Order
        fields = ['status']