from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from cinema.models import Ticket, Revenue, Movie, Expense, Inventory
from rest_framework.renderers import JSONRenderer
from cinema.serializers import TicketSerializer, RevenueSerializer, MovieSerializer, ExpenseSerializer, \
    InventorySerializer
from .serializers import TaxSerializer
from financial_report.models import Tax


# Create your views here.


class RevenueListView(APIView):
    serializer_class = RevenueSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'revenue.html'

    def get_queryset(self):
        return Revenue.objects.all()

    def get(self, request, *args, **kwargs):
        revenues = self.get_queryset()
        taxes = Tax.objects.all()
        serialized_data = self.serializer_class(revenues, many=True).data
        return Response({'revenues': serialized_data, 'taxes': taxes, 'date': timezone.now().date()})



class RevenueCreateView(APIView):
    serializer_class = RevenueSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cinema:revenue-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name='revenue.html')


class RevenueDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, revenue_id, format=None):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        revenue.delete()
        return Response({'message': 'Revenue deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='revenue.html')


class RevenueEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, revenue_id, format=None):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        serializer = RevenueSerializer(revenue)

        taxes = Tax.objects.all()
        tax_serializer = TaxSerializer(taxes, many=True)

        return Response({
            'revenue': serializer.data,
            'taxes': tax_serializer.data
        })

    def put(self, request, revenue_id, format=None):
        revenue = get_object_or_404(Revenue, id=revenue_id)
        serializer = RevenueSerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class RevenueEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, revenue_id):
        return render(request, 'revenue.html', {'revenue_id': revenue_id})


#-----------------------------------tickets--------------------------------------------------

class TicketListView(APIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'tickets.html'

    def get_queryset(self):
        return Ticket.objects.all()

    def get(self, request, *args, **kwargs):
        tickets = self.get_queryset()
        movies = Movie.objects.all()
        serialized_data = self.serializer_class(tickets, many=True).data
        return Response({'tickets': serialized_data, 'movies': movies, 'date': timezone.now().date()})



class TicketCreateView(APIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cinema:ticket-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, ticket_id, format=None):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.delete()
        return Response({'message': 'ticket deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='tickets.html')


class TicketEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, ticket_id, format=None):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        serializer = TicketSerializer(ticket)
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies, many=True)

        return Response({
            'tickets': serializer.data,
            'movies': movie_serializer.data
        })

    def put(self, request, ticket_id, format=None):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TicketEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, ticket_id):
        return render(request, 'tickets.html', {'ticket_id': ticket_id})

#-----------------------------------expense--------------------------------------------------

class ExpenseListView(APIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'expense.html'

    def get_queryset(self):
        return Expense.objects.all()

    def get(self, request, *args, **kwargs):
        expenses = self.get_queryset()
        expense_types = Expense.EXPENSE_TYPES
        serialized_data = self.serializer_class(expenses, many=True).data
        return Response({'expenses': serialized_data, 'expense_types': expense_types, 'date': timezone.now().date()})



class ExpenseCreateView(APIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cinema:expense-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, expense_id, format=None):
        expense = get_object_or_404(Expense, id=expense_id)
        expense.delete()
        return Response({'message': 'expense deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='expense.html')


class ExpenseEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, expense_id, format=None):
        expense = get_object_or_404(Expense, id=expense_id)
        serializer = ExpenseSerializer(expense)
        return Response({
            'expenses': serializer.data,
        })

    def put(self, request, expense_id, format=None):
        expense = get_object_or_404(Expense, id=expense_id)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ExpenseEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, expense_id):
        return render(request, 'expense.html', {'expense_id': expense_id})


#-----------------------------------inventory--------------------------------------------------

class InventoryListView(APIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]
    template_name = 'inventory.html'

    def get_queryset(self):
        return Inventory.objects.all()

    def get(self, request, *args, **kwargs):
        inventories = self.get_queryset()
        taxes = Tax.objects.all()
        inventory_data = []
        for inventory in inventories:
            tax_percentage = inventory.tax.tax_percentage
            total_cost_with_tax = inventory.quantity * inventory.cost + (
                        tax_percentage * inventory.cost * inventory.quantity / 100)
            serialized_inventory = self.serializer_class(inventory).data
            serialized_inventory['total_cost_with_tax'] = total_cost_with_tax
            inventory_data.append(serialized_inventory)

        # serialized_data = self.serializer_class(inventories, many=True).data
        return Response({'inventories': inventory_data, 'taxes': taxes, 'date': timezone.now().date()})



class InventoryCreateView(APIView):
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('cinema:inventory-list')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST, template_name='inventory.html')


class InventoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, inventory_id, format=None):
        inventory = get_object_or_404(Inventory, id=inventory_id)
        inventory.delete()
        return Response({'message': 'Inventory deleted successfully'}, status=status.HTTP_204_NO_CONTENT, template_name='inventory.html')


class InventoryEditAPIView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request, inventory_id, format=None):
        inventory = get_object_or_404(Inventory, id=inventory_id)
        serializer = InventorySerializer(inventory)

        taxes = Tax.objects.all()
        tax_serializer = TaxSerializer(taxes, many=True)

        return Response({
            'inventory': serializer.data,
            'taxes': tax_serializer.data
        })

    def put(self, request, inventory_id, format=None):
        inventory = get_object_or_404(Inventory, id=inventory_id)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class InventoryEditTemplateView(LoginRequiredMixin, View):
    def get(self, request, inventory_id):
        return render(request, 'inventory.html', {'inventory_id': inventory_id})

