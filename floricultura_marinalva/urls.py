from django.contrib import admin
from django.urls import path
from plantas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('login/', login_app, name='login'),
    path('planta/', lista_plantas, name='lista_plantas'),
    path('planta/<int:id>', exibir_planta, name='exibir_planta'),
    path('contatos/', contatos, name='contatos'),
    path('sobre/', sobre, name='sobre'),
    path('incluir_planta/', incluir_planta, name='incluir_planta'),
    path('editar_planta/<int:id>', editar_planta, name='editar_planta'),
    path('excluir_planta/<int:id>', excluir_planta, name='excluir_planta'),
    path('logout/', logout_app, name='logout'),
    path('cadastro/', cadastro_app, name='cadastro')
]