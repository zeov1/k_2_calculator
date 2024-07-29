from django import forms


class CalcForm(forms.Form):
    a = forms.FloatField(label='a')
    b = forms.FloatField(label='b')
    op = forms.CharField(label='op')
