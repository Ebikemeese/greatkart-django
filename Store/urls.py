from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    #for category slug
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    #for product slug
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    #for search functionality
    path('search/', views.search, name='search'),
    #for reviews
    path('submit_reviews/<int:product_id>/', views.submit_review, name='submit_review'),
] 