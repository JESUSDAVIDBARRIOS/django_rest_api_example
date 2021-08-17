from django.urls import path
from . import views

urlpatterns = [
    path('', views.vistaApi, name="vista-api"),
    path('lista-tareas/', views.listaTareas, name="lista-tareas"),
    path('detalle-tarea/<str:pk>/', views.detalleTarea, name="detalle-tarea"),
    path('crear-tarea/', views.crearTarea, name="crear-tarea"),
    path('actualizar-tarea/<str:pk>/', views.actualizarTarea, name="actualizar-tarea"),
    path('eliminar-tarea/<str:pk>/', views.eliminarTarea, name="eliminar-tarea")
]