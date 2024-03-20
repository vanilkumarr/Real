from django.shortcuts import render
from .models import Contact 
from .serializer import ContactSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from django.core.mail import send_mail
from rest_framework.response import Response
# Create your views here.
class ContactCreatView(APIView):
    permission_classes=(permissions.AllowAny,)

    def post(self,request,format=None):
        data=self.request.data
        try:
            send_mail(
                data['subject'],
                    'Name:'
                    +data['name']
                    +'\nEmail:'
                    +data['email']
                    +'\n\n\nPhone:'
                    +data['phone'],
                    'eziowilliams15@gmail.com',
                    ['eziowilliams15@gmail.com'],
                    fail_silently=False
            )
            contact=Contact(name=data['name'],email=data['email'],phone=data['phone'],subject=data['subject'])
            contact.save()
            return Response({'Successful'})
        except Exception as e:
            print(e)
            return Response({'error': 'Something went wrong'}, status=500)




