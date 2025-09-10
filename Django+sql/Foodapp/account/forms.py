from django import forms
from .models import Form_User

class User_Model_Form(forms.ModelForm):
    class Meta:
        model=Form_User
        fields=['name','email','password']