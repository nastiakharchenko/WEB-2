from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]                              #доступное количество единиц товара (доступны значения от 1 до 20)

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)          #TypedChoiceField - чтобы автоматически преобразовывать выбранное значение в целое число
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)     #обновить (значение True) или заменить (значение False) количество единиц для товара
                                                                                             #required - обязательный, initial - начальный, widget HiddenInput - чтобы пользователь не видел его в своей форме