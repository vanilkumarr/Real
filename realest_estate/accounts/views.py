from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User=get_user_model()
# Create your views here.   

class SignupView(APIView):
    permission_classes=(permissions.AllowAny,)

    def post(self,request,format=None):
        data =self.request.data
        name=data['name']
        email=data['email']
        password=data['password']
        password2=data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'err:email already exists'})
            else:
                if len(password)<6:
                    return Response({'err:passowrd is less than 6'})
                else:
                    user=User.objects.create_user(email=email,password=password,name=name)
                    user.save()
                    return Response({'success'})
        else:
            return Response({"Error:password doesnt match"})   