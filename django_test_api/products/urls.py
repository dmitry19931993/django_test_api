from django.urls import path
from .views import (
    ProductsListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductDetailView,
    ProductsDeleteAllView,
)

app_name = "products"


urlpatterns = [
    path("get", ProductsListView.as_view(), name="get"),
    path("create", ProductCreateView.as_view(), name="create"),
    path("update/<pk>/", ProductUpdateView.as_view(), name="update"),
    path("delete/<pk>/", ProductDeleteView.as_view(), name="delete"),
    path("<pk>/", ProductDetailView.as_view(), name="detail"),
    path("delete", ProductsDeleteAllView.as_view(), name="delete_all"),
]