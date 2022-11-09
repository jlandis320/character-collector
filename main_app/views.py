from django.shortcuts import render
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterUpdate(UpdateView):
  model = Character
  fields = [ 'media', 'description', 'age', 'pronoun']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  characters = Character.objects.all()
  return render(request, 'characters/index.html', {'characters': characters})

def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  return render(request, 'characters/detail.html', {'character' : character})