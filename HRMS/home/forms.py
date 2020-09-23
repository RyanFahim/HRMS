from django import forms
from .models import Employee,CVinfo

class Employeeform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

class cvform(forms.ModelForm):
    class Meta:
        model = CVinfo
        fields = '__all__'


