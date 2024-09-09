from django.db import models
from django.utils.translation import gettext as _

class Products(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )
    base_price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        null=True,
        blank=True,
    )
    image = models.ForeignKey(
        'catalog.ProductImages',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    parameter = models.ForeignKey(
        'catalog.ProductParameters',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    sort_by = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'Product: {self.name}'


class ProductImages(models.Model):
    image_name = models.CharField(
        _('Image Name'),
        max_length=1000,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        _('Image'),
        upload_to='product-image/',
        null=True,
        blank=True,
    )
    sort_by = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

    def __str__(self):
        return f'ProductImages: {self.image_name}'


class ProductParameters(models.Model):
    name = models.CharField(
        _('Image Name'),
        max_length=1000,
        null=True,
        blank=True,
    )
    value = models.FloatField(
        _('Value'),
        default=0.0,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        null=True,
        blank=True,
    )
    sort_by = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Product Parameter')
        verbose_name_plural = _('Product Parameters')

    def __str__(self):
        return f'ProductParameters: {self.name}'
