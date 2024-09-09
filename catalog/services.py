from catalog.models import Products


class ProductsService:
    def get_by_id(self, product_id: int) -> Products | None:
        return Products.objects.filter(id=product_id).first()
