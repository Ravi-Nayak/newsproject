from django import forms
from django.contrib.auth.models import User
#importing user form based model

class signForm(forms.ModelForm):
    class Meta:
        model=User #creating signup form based on this database table it means
        fields=['username','password','email','first_name','last_name']

