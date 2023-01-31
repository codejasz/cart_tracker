from uuid import uuid4

from django.db import models


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    external_id = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255)
    value = models.IntegerField()  # store prices in cents to avoid floating point issue
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'external_id'], name='unique item ID within cart'
            )
        ]

    def __str__(self):
        # divide value by 100 to display actual price of item
        return f'{self.name} {self.value/100:.2f}'
