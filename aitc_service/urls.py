from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('pelayanan/', include('pelayanan.urls')),
    path('kategori/', include('master.urls')),

    path('user/', views.userPage, name='user-page'),
]
