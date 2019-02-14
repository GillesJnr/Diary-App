from django.urls import path
from . import views


urlpatterns = [
    path('', views.create, name="create"),
    path('<int:id>', views.create, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
]
