from django.urls import path
from .views import spell_check
from . import views

urlpatterns = [
    path('', spell_check, name='spell_check'),
    path('spell_check/', spell_check, name='spell_check'),
]