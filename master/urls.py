from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', kategori, name='kategori'),
    path('editkategori/<str:pk>/', views.editkategori, name='editkategori'),
    path('kategori/kategoridel/<str:pk>/', views.kategoridel, name='kategoridel'),
]
