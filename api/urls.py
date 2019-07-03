from django.urls import path, include
from .views import tecnolgia_view

urlpatterns = [
    path('tecnologias/', tecnolgia_view.TecnologiaList.as_view(), name='tecnologia-list'),
]
