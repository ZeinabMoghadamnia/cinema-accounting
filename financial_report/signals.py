from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import DailyReport
from cinema.models import Revenue, Expense
from vendor.models import Purchase
from financial_report.models import Tax
from django.db.models import Sum, F


def update_or_create_daily_report(report_date):
    total_revenue = Revenue.objects.filter(date=report_date).aggregate(
        ticket_sale=Sum('ticket_sale'),
        concession_sale=Sum('concession_sale'),
        other_income=Sum('other_income')
    )
    total_revenue = (total_revenue['ticket_sale'] or 0) + (total_revenue['concession_sale'] or 0) + (
            total_revenue['other_income'] or 0)
    total_expense = Expense.objects.filter(date=report_date).aggregate(total=Sum('amount'))['total'] or 0
    purchase_total = Purchase.objects.filter(date=report_date).aggregate(
        total=Sum(F('cost') * F('quantity'))
    )['total'] or 0
    taxes = Tax.objects.filter(date=report_date, tax_type='cinema tax').aggregate(total=Sum('tax_percentage'))[
                'total'] or 0
    total_taxes = total_revenue * taxes / 100

    profit = total_revenue - (total_expense + purchase_total + total_taxes)

    daily_report, created = DailyReport.objects.get_or_create(date=report_date, defaults={'profit': profit,
                                                                                          'total_revenue': total_revenue,
                                                                                          'total_expense': total_expense,
                                                                                          'total_taxes': total_taxes, })

    daily_report.total_revenue = total_revenue
    daily_report.total_expense = total_expense + purchase_total
    daily_report.total_taxes = total_taxes
    daily_report.profit = profit
    daily_report.save()


@receiver(post_save, sender=Revenue)
@receiver(post_save, sender=Expense)
@receiver(post_save, sender=Purchase)
@receiver(post_save, sender=Tax)
def update_daily_report_on_change(sender, instance, created, **kwargs):
    report_date = instance.date
    update_or_create_daily_report(report_date)
