from django import forms
from assignment4.models import StuModel
from assignment4.models import CorModel

class Stuforms(forms.ModelForm):
    class Meta:
        model = StuModel
        fields="__all__"
class Corforms(forms.ModelForm):
    class Meta:
        model = CorModel
        fields="__all__"