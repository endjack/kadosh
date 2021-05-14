
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from membros.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(MembroListView.as_view()), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('criar/', login_required(MembroCreateView.as_view()), name='criar_membro'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    
]
