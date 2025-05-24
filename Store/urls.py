from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    #for category slug
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    #for product slug
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
] 