from django import forms


class AddToCartProductForm(forms.Form):
    Quantity_CHOICES = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(choices=Quantity_CHOICES, coerce=int)

    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
