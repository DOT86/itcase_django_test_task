from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(
    r'catalog/products',
    views.ProductsViewSet,
    basename='products'
)

urlpatterns = [
    path(
        'catalog/get-products/<int:product_id>/',
        views.GetProductAPIView.as_view(),
        name='get-product',
    ),
    path('', include(router.urls)),
]
