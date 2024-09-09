from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from catalog.filters import ProductsFilter
from catalog.models import Products
from catalog.serializers import ProductsSerializer, FullParametersProductsSerializer
from catalog.services import ProductsService


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductsFilter


class GetProductAPIView(views.APIView):
    @swagger_auto_schema(responses={200: FullParametersProductsSerializer(), 204: '{}'})
    def gey(self, request):
        product_id = request.GET.get('product_id')
        product_service = ProductsService()
        product = product_service.get_by_id(product_id)
        if product:
            serializer = FullParametersProductsSerializer(instance=product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)


