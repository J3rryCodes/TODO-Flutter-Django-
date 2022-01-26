from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from core.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

from core.models import UserProfileModel

class LoginView(APIView):

    def post(setf,request,format=None):
        ''' LOGIN View '''

        email = request.data['email']
        password = request.data['password']

        user = UserProfileModel.objects.get(email=email)

        if user.check_password(password):
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)

            user_serializer = UserProfileSerializer(instance=user)

            return Response({"user_data": user_serializer.data ,"status" : True,"token":token.pk})

        return Response({"status":False })



class RegistratrionView(APIView):
    ''' Registration View'''

    def post(self,request,format=None):
        ''' Register a user '''

        user_serializer = UserProfileSerializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.create(user_serializer.validated_data)
            token = Token.objects.create(user=user)

            user_serializer = UserProfileSerializer(instance=user)

            return Response({"user_data": user_serializer.data,"status":True , 'tokn' : token.pk})
        else:
            return Response({"status":False })



class LogoutView(APIView):
    ''' User Logout view '''

    permission_classes = (IsAuthenticated,)

    def post(self,request,format=None):
        ''' Log out a user '''

        request.user.auth_token.delete()
        return Response({'status':True})
