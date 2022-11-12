from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Character, Medium
from .forms import TitleForm

class Home(LoginView):
  template_name = 'home.html'

class CharacterCreate(LoginRequiredMixin, CreateView):
  model = Character
  fields = ['name', 'media', 'description', 'age', 'pronoun']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CharacterUpdate(LoginRequiredMixin, UpdateView):
  model = Character
  fields = [ 'media', 'description', 'age', 'pronoun']

class CharacterDelete(LoginRequiredMixin, DeleteView):
  model = Character
  success_url = '/characters/'

class MediumCreate(LoginRequiredMixin, CreateView):
  model = Medium
  fields = '__all__'

class MediumList(LoginRequiredMixin, ListView):
  model = Medium

class MediumDetail(LoginRequiredMixin, DetailView):
  model = Medium

class MediumUpdate(LoginRequiredMixin, UpdateView):
  model = Medium
  fields = ['medium', 'color']

class MediumDelete(LoginRequiredMixin, DeleteView):
  model = Medium
  success_url = '/mediums/'



def about(request):
  return render(request, 'about.html')

@login_required
def characters_index(request):
  characters = Character.objects.filter(user=request.user)
  return render(request, 'characters/index.html', {'characters': characters})

@login_required
def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  medium_character_doesnt_have = Medium.objects.exclude(id__in = character.medium.all().values_list('id'))
  title_form = TitleForm()
  return render(request, 'characters/detail.html', {'character' : character, 'title_form': title_form, 'medium': medium_character_doesnt_have})

@login_required
def add_title(request, character_id):
  form = TitleForm(request.POST)
  if form.is_valid():
    new_title = form.save(commit=False)
    new_title.character_id = character_id
    new_title.save()
  return redirect('characters_detail', character_id=character_id)

@login_required
def assoc_medium(request, character_id, medium_id):
  Character.objects.get(id=character_id).medium.add(medium_id)
  return redirect('characters_detail', character_id=character_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('characters_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})