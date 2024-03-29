from django.contrib import admin
from django.urls import path, include
from acolhe.views import geral, anfitriao, acolhido, local

urlpatterns = [
   path('', geral.home_view, name='home'),
   path('acolhido/', include(([
      path('', acolhido.home_acolhido, name = 'home_acolhido'),
      path('cadastrar', acolhido.cadastrar_view, name='cadastrar_acolhido'),
   ], 'acolhe'), namespace='acolhido')
   ),

   path('local/<int:id>/solicitar', local.solicitar_view, name='local_solicitar'),
   path('local/<int:id>/cancelar', local.cancelar_view, name='local_cancelar'),
   path('local/<int:id>/aprovar', local.aprovar_view, name='local_disponivel'),
   path('local/<int:id>/disponivel', local.disponivel_view, name='local_disponivel'),
   path('local/<int:id>/detalhes', local.detalhes_view, name='detalhes_view'),
   path('local/<int:pk>/comment/', local.add_comment_to_local, name='add_comment_to_local'),

   path('anfitriao/', include(([
      path('', anfitriao.home_anfitriao, name = 'home_anfitriao'),
      path('cadastrar', anfitriao.cadastrar_view, name='cadastrar_anfitriao'),
      path('local', anfitriao.cadastrar_local_view, name='cadastrar_local'),
      path('local/<pk>/remover', anfitriao.remover_view, name='remover_view'),
      path('local/<pk>/editar/',anfitriao.editar_view, name='editar_view'),
      path('local/<int:id>/detalhes', anfitriao.anfitriao_detalhes_view, name='anfitriao_detalhes_view'),
      path('local/<int:pk>/comment/', anfitriao.add_comment_to_local_anfitriao, name='add_comment_to_local_anfitriao'),
   ], 'acolhe'),namespace='anfitriao')
   ),

   path('login/', geral.login_view, name='login'),
   path('logout/', geral.logout_view, name='logout'),
]