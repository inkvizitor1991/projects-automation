from django.urls import path

from . import views


app_name = "integrationapp"

urlpatterns = [
    path('trello/<int:project_id>', views.handle_trello_create_request, name="trello"),
    path('discord/', views.create_discord, name="discord"),
]
