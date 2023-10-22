from django.urls import path

from .views import visit_create_view

app_name = 'visit'

urlpatterns = [
    path('create/', visit_create_view, name='create'),
]