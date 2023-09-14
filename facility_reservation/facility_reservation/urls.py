from django.contrib import admin
from django.urls import path,include
from wallet import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('',include("wallet.urls")),
    path('special/', views.special, name='special'),
    path('wallet/', include('wallet.urls')),
    path('logout/', views.user_logout, name='logout'),
]