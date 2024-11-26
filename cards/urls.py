from django.urls import path
from . import views
# from django.views.generic import TemplateView


urlpatterns = [
    # path("", views.index, name="index"),
    # path("", TemplateView.as_view(template_name="cards/layout.html"), name="index"),
    path("", views.CardListView.as_view(), name="card-list"),
    path("new", views.CardCreateView.as_view(), name="card-create"),
    path("edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
    path("delete/<int:pk>", views.CardDeleteView.as_view(), name="card-delete"),
]
