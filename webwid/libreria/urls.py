from django.urls import path
from . import views

urlpatterns = [

 path('', views.inicio, name='inicio'),
 path('page', views.pagina, name='page'),
 path('plantas', views.plantas, name='plantas'),
 path('crear', views.crear, name='crear'),
 path('editar', views.editar, name='editar')

]