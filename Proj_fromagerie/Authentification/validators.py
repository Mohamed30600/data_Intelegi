from ast import For
from curses.ascii import isalpha
from wsgiref.validate import validator
from django.core.exceptions import ValidationError
from . import forms
from . import validators

class ContainsLetterValidator:
    def validate(self,password,user=None):#mmethode validate verifi le mot de passe et provoque une erreur si pb 
        if not any(char.isalpha() for char in password):
            raise ValidationError (
                'le mot de passe doit contenir une lettre ', code='password_no_letter'
            )
    def get_help_text(self):
        return 'votr mot de passe doi contenir au moins une lettre .'


class PostCodeForm(forms.Form):
    post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])