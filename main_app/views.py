from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Character, Medium
from .forms import TitleForm

class Home(LoginView):
  template_name = 'home.html'

class CharacterCreate(CreateView):
  model = Character
  fields = ['name', 'media', 'description', 'age', 'pronoun']

class CharacterUpdate(UpdateView):
  model = Character
  fields = [ 'media', 'description', 'age', 'pronoun']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters/'

class MediumCreate(CreateView):
  model = Medium
  fields = '__all__'

class MediumList(ListView):
  model = Medium

class MediumDetail(DetailView):
  model = Medium

class MediumUpdate(UpdateView):
  model = Medium
  fields = ['medium', 'color']

class MediumDelete(DeleteView):
  model = Medium
  success_url = '/mediums/'

# def home(request):
#   return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  characters = Character.objects.all()
  return render(request, 'characters/index.html', {'characters': characters})

def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  medium_character_doesnt_have = Medium.objects.exclude(id__in = character.medium.all().values_list('id'))
  title_form = TitleForm()
  return render(request, 'characters/detail.html', {'character' : character, 'title_form': title_form, 'medium': medium_character_doesnt_have})

def add_title(request, character_id):
  form = TitleForm(request.POST)
  if form.is_valid():
    new_title = form.save(commit=False)
    new_title.character_id = character_id
    new_title.save()
  return redirect('characters_detail', character_id=character_id)

def assoc_medium(request, character_id, medium_id):
  Character.objects.get(id=character_id).medium.add(medium_id)
  return redirect('characters_detail', character_id=character_id)