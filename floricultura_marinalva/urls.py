from django.contrib import admin
from django.urls import path
from plantas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('login/', login_app, name='login'),
    path('planta/', lista_plantas, name='lista_plantas'),
    path('planta/<int:id>', exibir_planta, name='exibir_planta'),
    path('contatos', contatos, name='contatos'),
    path('sobre', sobre, name='sobre'),
]