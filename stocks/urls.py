from django.urls import path
 
from . import views
 
app_name = 'stocks'
urlpatterns = [
    path('stocks/', views.StockIndexView.as_view(), name='index'),
    path('stocks/create/', views.StockCreateView.as_view(), name='create'),
]