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
        date = request.data.get("date")
        try:
            todo_list = []
            if date is None:
                todo_list = TODOModel.objects.filter(user=user)
            else:
                todo_list = TODOModel.objects.filter(date=date,user=user)
                
            todo_serializer = TODOModelSeralizer(instance=todo_list,many=True)

            return Response({'status':True,'todo_list':todo_serializer.data})
        except TODOModel.DoesNotExist:
            return Response({'status':True,'todo_list':[]})


    def retrieve(self,request,pk):
        """ Get one TODO with currosponding ID"""

        user = UserProfileModel.objects.get(email=request.user)
        try:
            todo= TODOModel.objects.get(id=pk,user=user)
            todo_serializer = TODOModelSeralizer(instance=todo)
            
            Response({"status":True,"error" :"","todo":todo_serializer.data})
        except TODOModel.DoesNotExist:
            return Response({"status":False,"error" :"ToDo not found"})

    
    def partial_update(self,request,pk):
        """" Edit TODO By ID """

        user = UserProfileModel.objects.get(email=request.user)
        try:
            todo = TODOModel.objects.get(id=pk,user=user)
            todo.is_completed = request.data.get('is_completed',todo.is_completed )
            todo.title = request.data.get('title',todo.title)
            todo.description = request.data.get('description',todo.description)
            todo.date = request.data.get('date',todo.date)
            todo.save()
            todo_serializer = TODOModelSeralizer(instance=todo)
            return Response({"status":True,"error" :"","todo":todo_serializer.data})
        except TODOModel.DoesNotExist:
            return Response({"status":False,"error" : "ToDo not found"})


    def create(self,request):

        todo_serializer = TODOModelSeralizer(data=request.data)

        print(todo_serializer.initial_data)

        if todo_serializer.is_valid(raise_exception=True):
           data = todo_serializer.save(user=request.user)
           print(data)
           return Response({'status':True,"error":""})
        else:
           return Response({'status':False,"error":"Something went to an error"})


    def destroy(self,request,pk):
        """ Delete a todo by ID """
        user = UserProfileModel.objects.get(email=request.user)
        try:
            todo = TODOModel.objects.get(id=pk,user=user)
            todo.delete()
            return Response({"status":True,"error" :""})

        except TODOModel.DoesNotExist:
            return Response({"status":False,"error" : "ToDo not found"})


            

        




