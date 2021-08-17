from django.views.generic import ListView, DetailView

from items.models import Item

from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from accounts.forms import CustomUserCreationForm
# Create your views here.

class ItemListView(ListView):
  template_name = "items.html"
  model = Item
  
class ItemDetailView(DetailView):
  template_name = "item_detail.html"
  model = Item