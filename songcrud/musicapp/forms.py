from django import forms  
from musicapp.models import Artiste
class ArtisteForm(forms.ModelForm):  
    class Meta:  
        model = Artiste
        fields = "__all__"  