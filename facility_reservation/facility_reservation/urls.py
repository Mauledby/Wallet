from django.contrib import admin
from django.urls import path, include
from wallet import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wallet/', include('wallet.urls', namespace='wallet')),  # Include app-specific URLs with the 'wallet' namespace
    path('walletAPI/', include(('walletAPI.urls', 'walletAPI'), namespace='walletAPI')),
    path('' , views.IndexView.as_view(), name='index'),
    
    
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='wallet/password_reset.html'), name="password_reset"),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='wallet/password_reset_done.html'), name = "password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='wallet/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='wallet/password_reset_complete.html'), name='password_reset_complete')
]
