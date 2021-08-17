from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TareaSerializer
from .models import *

# Create your views here.

@api_view(['GET'])
def vistaApi(request):
    api_urls = {
        'Lista': '/lista-tareas/',
        'Vista Detalle': '/detalle-tarea/<str:pk>/',
        'Crear': '/crear-tarea/',
        'Actualizar': '/actualizar-tarea/<str:pk>/',
        'Eliminar': '/eliminar-tarea/<str:pk>/'
    }

    return Response(api_urls)

@api_view(['GET'])
def listaTareas(request):
    tareas = Tarea.objects.all()
    serializer = TareaSerializer(tareas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalleTarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    serializer = TareaSerializer(tarea, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def crearTarea(request):
    serializer = TareaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def actualizarTarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    serializer = TareaSerializer(instance=tarea, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def eliminarTarea(request, pk):
    tarea = Tarea.objects.get(id=pk)
    tarea.delete()
    return Response('¡Se eliminó correctamente la tarea!')

