from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from employee_management.models import Payroll, EmployeePerformance
from django.db.models import Sum


@receiver(post_save, sender=Payroll)
def calculate_net_salary(sender, instance, **kwargs):
    current_month = timezone.now().month
    current_year = timezone.now().year

    performance = EmployeePerformance.objects.filter(
        employee=instance.employee,
        date__year=current_year,
        date__month=current_month,
    ).values('performance_type').annotate(total_hours=Sum('number_of_hours'))

    overtime_hours = 0
    absence_hours = 0

    for perf in performance:
        if perf['performance_type'] == 'overtime':
            overtime_hours = perf['total_hours']
        elif perf['performance_type'] == 'absence':
            absence_hours = perf['total_hours']

    overtime_adjustment = overtime_hours * (1.5 * (instance.salary / 160))
    absence_adjustment = absence_hours * (instance.salary / 160)

    tax_amount = instance.tax.tax_percentage if instance.tax and instance.tax.tax_type=='employee tax' else 0
    net_salary = instance.salary - (instance.salary * tax_amount / 100) + overtime_adjustment - absence_adjustment

    Payroll.objects.filter(pk=instance.pk).update(net_salary=net_salary)
