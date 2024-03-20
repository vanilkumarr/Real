from .views import ContactCreatView
from django.urls import path

urlpatterns = [
    path('',ContactCreatView.as_view()),
]
