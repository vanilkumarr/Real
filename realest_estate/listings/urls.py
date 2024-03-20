from django.urls import path
from .views import ListingsViews,ListingView,SearchView

urlpatterns = [
    path('',ListingsViews.as_view()),
    path('search/',SearchView.as_view()),
    path('<slug>',ListingView().as_view()),
    
]
