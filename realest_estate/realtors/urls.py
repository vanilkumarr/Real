from .views import RealtorListViews,TopsellerView,RealtorView
from django.urls import path

urlpatterns = [
    path("",RealtorListViews.as_view()),
    path("topseller",TopsellerView.as_view()),
    path('<pk>',RealtorView.as_view())
]
