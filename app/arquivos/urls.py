from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("excluir/<int:pk>/", views.excluir, name="excluir"),
]
