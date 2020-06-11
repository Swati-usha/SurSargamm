from django.forms import ModelForm
from .models import MySongs


class  CreateForm(ModelForm):
    class Meta:
        model = MySongs
        fields = ['PlaylistName','Link','Favourite']
