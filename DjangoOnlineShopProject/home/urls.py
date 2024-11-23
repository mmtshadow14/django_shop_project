from django.urls import path
from .views import HomeView, ProductDetailView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]






