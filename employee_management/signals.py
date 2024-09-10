from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from employee_management.models import Payroll, EmployeePerformance
from django.db.models import Sum


@receiver(post_save, sender=EmployeePerformance)
def update_payroll(sender, instance, **kwargs):
    # Get the employee's payroll for the current month and year
    current_month = timezone.now().month
    current_year = timezone.now().year
    payroll, created = Payroll.objects.get_or_create(
        employee=instance.employee,
        date__year=current_year,
        date__month=current_month,
        defaults={'salary': 0, 'net_salary': 0}
    )

    # Calculate total overtime and absence hours for the employee in the current month
    performance = EmployeePerformance.objects.filter(
        employee=instance.employee,
        date__year=current_year,
        date__month=current_month
    ).values('performance_type').annotate(total_hours=Sum('number_of_hours'))

    # Initialize overtime and absence variables
    overtime_hours = 0
    absence_hours = 0

    for perf in performance:
        if perf['performance_type'] == 'overtime':
            overtime_hours = perf['total_hours']
        elif perf['performance_type'] == 'absence':
            absence_hours = perf['total_hours']

    # Calculate overtime and absence adjustment
    overtime_adjustment = overtime_hours * (1.5 * (payroll.salary / 160))  # Assuming 160 hours per month
    absence_adjustment = absence_hours * (payroll.salary / 160)  # Assuming 160 hours per month

    # Update salary with adjustments
    adjusted_salary = payroll.salary + overtime_adjustment - absence_adjustment

    # Calculate net salary after tax deduction
    tax_percentage = payroll.tax.tax_percentage  # Make sure to have an amount field in Tax model
    net_salary = adjusted_salary - (adjusted_salary * tax_percentage / 100)

    # Update payroll with new net salary
    payroll.net_salary = net_salary
    payroll.save()
