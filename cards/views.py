from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Card


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")


class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")


class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy("card-list")
