from django.urls import path

from products.views import CategoryView, ProductView, ProductListView

urlpatterns = [
    path('/categories', CategoryView.as_view()),
    path('/<int:product_id>', ProductView.as_view()),
    path('', ProductListView.as_view())
]