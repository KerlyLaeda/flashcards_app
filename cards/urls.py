from django.urls import path
from . import views
# from django.views.generic import TemplateView


urlpatterns = [
    # path("", views.index, name="index"),
    # path("", TemplateView.as_view(template_name="cards/layout.html"), name="index"),
    path("", views.CardListView.as_view(), name="card_list"),
]
