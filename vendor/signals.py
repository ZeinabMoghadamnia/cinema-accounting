from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Purchase
from cinema.models import Inventory

@receiver(post_save, sender=Purchase)
def update_inventory_on_purchase(sender, instance, created, **kwargs):
    if created:
        try:
            inventory_item = Inventory.objects.get(item_name=instance.item_name, cost=instance.cost)
            inventory_item.quantity += instance.quantity
            inventory_item.date = instance.date
            inventory_item.save()
        except Inventory.DoesNotExist:
            Inventory.objects.create(
                item_name=instance.item_name,
                quantity=instance.quantity,
                cost=instance.cost,
                tax=instance.tax,
                date=instance.date
            )