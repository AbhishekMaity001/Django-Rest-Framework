from django.http import JsonResponse
from django.shortcuts import render
from itsdangerous import Serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    """This is just a basic api Overview which will return all the url routes our application is having"""
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>',
    }
    
    # return JsonResponse("API BASE POINT", safe=False)
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    """This will list down all the tasks available"""
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    """This will just fetch the tasks based on the id"""
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    # In model forms we do request.post but since this is an API view so we have access to request.data
    # request.data will send you the json object
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data) # Instead of creating a new item we will update the old item
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item id : {} --> Successfully deletedddddddd'.format(pk))

@api_view(['DELETE'])
def taskDelete(request):
    task = Task.objects.all()
    task.delete()
    return Response('ALL ITEMS DELETED')