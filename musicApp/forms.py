from django.forms import ModelForm
from .models import mainForm


class mainForm(ModelForm):
    class Meta:
        model = mainForm
        fields = [
            'album_name',
            'artist_name',
            'genre',
        ]