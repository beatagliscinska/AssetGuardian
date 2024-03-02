from django.test import TestCase
from viewer.models import Asset, AssetCategory, Employee


class TestModels(TestCase):
    def setUp(self):
        # Create an AssetCategory instance
        self.category = AssetCategory.objects.create(name='Test Category')
        # Create an Employee instance
        self.employee = Employee.objects.create(name='Test', surname='Employee', position='Position', department='Department', manager='Manager')

    def test_asset_model(self):
        # Use the created AssetCategory and Employee instances when creating the Asset object
        asset = Asset.objects.create(category=self.category, description='Test Asset', vendor='Vendor', serial_number='123', value=100, purchase_date='2023-01-01', assigned_to=self.employee)
        self.assertEqual(str(asset), 'Test Asset')

    def test_employee_model(self):
        employee = Employee.objects.create(name='Test', surname='Employee', position='Position', department='Department', manager='Manager')
        self.assertEqual(str(employee), 'Test')