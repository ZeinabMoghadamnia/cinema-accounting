from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Inventory, Tax
from django.contrib.auth.models import User
from employee_management.models import CustomUser

# Create your tests here.

class InventoryModelTest(TestCase):
    def setUp(self):
        self.tax = Tax.objects.create(tax_percentage=10)

        self.inventory = Inventory.objects.create(
            item_name='Test Item',
            quantity=10,
            cost=100,
            tax=self.tax,
            date=timezone.now()
        )

    def test_inventory_creation(self):
        self.assertEqual(self.inventory.item_name, 'Test Item')
        self.assertEqual(self.inventory.quantity, 10)
        self.assertEqual(self.inventory.cost, 100)
        self.assertEqual(self.inventory.tax, self.tax)

    def test_inventory_str_method(self):
        self.assertEqual(str(self.inventory), 'Test Item')


class InventoryListViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = CustomUser.objects.create_user(email='testuser', phone_number='09005566444',first_name='aaa',last_name='bbb', password='testpassword')

        self.tax = Tax.objects.create(tax_percentage=10)
        self.inventory = Inventory.objects.create(
            item_name='Test Item',
            quantity=10,
            cost=100,
            tax=self.tax,
            date=timezone.now()
        )
        self.list_url = reverse('cinema:inventory-list')

    def test_inventory_list_view_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class InventoryCreateViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.tax = Tax.objects.create(tax_percentage=10)
        self.create_url = reverse('cinema:inventory-create')

    def test_create_inventory(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', phone_number='09005566444',
                                                   first_name='aaa', last_name='bbb', password='testpassword')

        self.client.force_authenticate(user=self.user)

        data = {
            'item_name': 'New Item',
            'quantity': 5,
            'cost': 200,
            'tax_id': self.tax.id
        }

        response = self.client.post(self.create_url, data)

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            print(response.data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Inventory.objects.count(), 1)
        self.assertEqual(Inventory.objects.get().item_name, 'New Item')

class InventoryDeleteViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.tax = Tax.objects.create(tax_percentage=10)
        self.inventory = Inventory.objects.create(
            item_name='Test Item',
            quantity=10,
            cost=100,
            tax=self.tax,
            date=timezone.now()
        )
        self.delete_url = reverse('cinema:inventory-delete', args=[self.inventory.id])

    def test_delete_inventory(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', phone_number='09005566444',
                                                   first_name='aaa', last_name='bbb', password='testpassword')
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Inventory.objects.count(), 0)


class InventoryEditAPIViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = CustomUser.objects.create_user(email='testuser@example.com', phone_number='09005566444', first_name='aaa', last_name='bbb', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.tax = Tax.objects.create(tax_percentage=10)
        self.inventory = Inventory.objects.create(
            item_name='Test Item',
            quantity=10,
            cost=100,
            tax=self.tax,
            date=timezone.now()
        )

        self.edit_url = reverse('cinema:inventory-edit-api', args=[self.inventory.id])

    def test_get_inventory(self):
        response = self.client.get(self.edit_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('inventory', response.data)
        self.assertIn('taxes', response.data)

        inventory_data = response.data['inventory']
        self.assertEqual(inventory_data['item_name'], 'Test Item')
        self.assertEqual(inventory_data['quantity'], 10)

        taxes_data = response.data['taxes']
        self.assertEqual(len(taxes_data), 1)
        self.assertEqual(taxes_data[0]['tax_percentage'], 10)

    def test_put_inventory(self):
        updated_data = {
            'item_name': 'Updated Item',
            'quantity': 20,
            'cost': 150,
            'tax_id': self.tax.id
        }

        response = self.client.put(self.edit_url, updated_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.inventory.refresh_from_db()
        self.assertEqual(self.inventory.item_name, 'Updated Item')
        self.assertEqual(self.inventory.quantity, 20)
        self.assertEqual(self.inventory.cost, 150)