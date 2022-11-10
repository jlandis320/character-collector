from django.db import models
from django.urls import reverse

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  media = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.CharField(max_length=20)
  pronoun = models.CharField(max_length=10)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('characters_detail', kwargs={'character_id': self.id})


class Title(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField('Release Date')
  character = models.ForeignKey(Character, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.title} ({self.date})"
  
  class Meta: 
    ordering = ['-date']