from django import forms
from .models import *
from django.core.validators import URLValidator

class SenderoForm(forms.Form):
	nombre = forms.CharField(max_length=80)
	duracion = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
	descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":50}))
	url = forms.CharField(required=False, validators=[URLValidator()])
	alt = forms.CharField(max_length=80, required=False)


class LoginForm(forms.Form):
	username = forms.CharField(max_length=80)
	password = forms.CharField(max_length=80, widget=forms.PasswordInput())


