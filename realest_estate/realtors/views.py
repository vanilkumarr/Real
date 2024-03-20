from django.shortcuts import render
from .serializer import RealtorsSerializer
from .models import Realtors
from rest_framework import permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.


class RealtorListViews(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset=Realtors.objects.all()
    serializer_class=RealtorsSerializer
    pagination_class=None

class RealtorView(RetrieveAPIView):
    queryset=Realtors.objects.all()
    serializer_class=RealtorsSerializer

class TopsellerView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset=Realtors.objects.filter(top_seller=True)
    serializer_class=RealtorsSerializer
    pagination_class=None