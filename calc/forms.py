from django import forms


class CalcForm(forms.Form):
    a = forms.CharField(label='a', empty_value='0')
    b = forms.CharField(label='b', empty_value='0')
    op = forms.CharField(label='op')
