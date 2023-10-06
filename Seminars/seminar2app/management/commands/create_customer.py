from django.core.management.base import BaseCommand
from seminar2app.models import Customer


class Command(BaseCommand):
    help = 'create customer, accepts "name email phone address"'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='customername')
        parser.add_argument('email', type=str, help='customer email')
        parser.add_argument('phone_number', type=str, help='customer phone number')
        parser.add_argument('address', type=str, help='customer_address_use_snakecase')

    def handle(self, *args, **kwargs):
        customer = Customer(name=kwargs['name'],
                            email=kwargs['email'],
                            phone_number=kwargs['phone_number'],
                            address=kwargs['address'])
        customer.save()
        self.stdout.write(str(customer))
