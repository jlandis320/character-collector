from django.forms import ModelForm
from .models import Title

class TitleForm(ModelForm):
  class Meta:
    model = Title
    fields = ['date', 'title']