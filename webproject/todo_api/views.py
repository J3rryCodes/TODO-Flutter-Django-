from django.http import request
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from todo_api.models import TODOModel
from todo_api.serializers import TODOModelSeralizer
from core.models import UserProfileModel


class TODOView(ViewSet):
    """View for TODO Model"""

    permission_classes = (IsAuthenticated,)

    def list(self,request,**kwargs):
        """List all TODOS By Date"""

        user = UserProfileModel.objects.get(email=request.user)
        date = request.data['date']
        todo_list = TODOModel.objects.filter(date=date,user=user)

        todo_serializer = TODOModelSeralizer(instance=todo_list,many=True)

        return Response({'status':True,'todo_list':todo_serializer.data})
        


