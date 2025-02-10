from django.urls import path
from .views import *

urlpatterns = [
    path("skill-view/", skill_view, name="skill_view"),
]
