import random

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


class BoxView(CardListView):
    template_name = "cards/box.html"

    # only return the cards where the box number matches the box_num value
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]

        # Present random card from selected box, if it's not empty
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)

        return context
