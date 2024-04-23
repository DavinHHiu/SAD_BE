from django.db import models


class CartItem(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField(
        blank=True,
        null=True,
        default=None,
    )
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    image = models.ImageField()
    total_price = models.FloatField()

    def augment_quantity(self, quantity):
        self.quantiy += quantity
        self.save()

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)
