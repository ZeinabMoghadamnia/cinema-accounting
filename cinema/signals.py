from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from .models import Ticket, Revenue, Inventory


@receiver(post_save, sender=Ticket)
def update_revenue_on_ticket_save(sender, instance, **kwargs):
    total_ticket_sales = Ticket.objects.filter(date=instance.date).aggregate(total_sales=Sum('price'))[
                             'total_sales'] or 0
    concession_sale = Inventory.objects.filter(date=instance.date).aggregate(total_sales=Sum('cost'))[
                          'total_sales'] or 0

    Revenue.objects.update_or_create(
        date=instance.date,
        defaults={'ticket_sale': total_ticket_sales, 'concession_sale': concession_sale}
    )
