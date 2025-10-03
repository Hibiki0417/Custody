from django.urls import path 
from . import views

app_name = 'crm'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/create/',views.CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/detail/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),
    path('customers/<int:pk>/update/',views.CustomerUpdateView.as_view(), name='customer_update'),
]
