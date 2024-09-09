from rest_framework import serializers
from catalog.models import (
    Products,
    ProductImages,
    ProductParameters
)


class ProductImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(
        'get_image_url',
    )

    def get_image_url(self, obj: ProductImages) -> str | None:
        if obj.image:
            return f'{obj.image.url}'

    class Meta:
        model = ProductImages
        fields = [
            'id',
            'image_name',
            'image_url',
            'sort_by'
        ]


class ProductParametersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductParameters
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'description',
            'base_price',
        ]


class FullParametersProductsSerializer(serializers.ModelSerializer):
    image_id = serializers.PrimaryKeyRelatedField(
        source='image',
        queryset=ProductImages.objects.all(),
        required=False,
        allow_null=True,
    )
    image = ProductImagesSerializer(read_only=True)
    parameter_id = serializers.PrimaryKeyRelatedField(
        source='parameter',
        queryset=ProductParameters.objects.all(),
        required=False,
        allow_null=True,
    )
    parameter = ProductParametersSerializer(read_only=True)

    class Meta:
        model = Products
        fields = [
            'id',
            'name',
            'description',
            'base_price',
            'image_id',
            'image',
            'parameter_id',
            'parameter',
            'sort_by'
        ]
