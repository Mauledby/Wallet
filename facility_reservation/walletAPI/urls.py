from django import views
from django.urls import path
from walletAPI.views import login_view, CreateVendorTransactionView,TransactionReceiptView,logout_view

app_name = 'walletAPI'

urlpatterns = [
    path('login/', login_view, name='login'),
    # Define other URL patterns for your API views
    path('create-transaction/', CreateVendorTransactionView.as_view(), name='create-transaction'),
    path('receipt/', TransactionReceiptView.as_view(), name='transaction_receipt'),
    path('logout/', logout_view, name='logout'),
]
