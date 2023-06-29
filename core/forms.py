from django import forms 
from .models import Alligator


class NewAlligatorForm(forms.ModelForm):

   class Meta: 
      model = Alligator
      fields = "__all__" 
