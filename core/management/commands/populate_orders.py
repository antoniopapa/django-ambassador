from django.core.management import BaseCommand
from faker import Faker
from random import randrange
from core.models import Order, OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(3):
            order = Order.objects.create(
                user_id=35,
                code='code',
                ambassador_email='b@b.com',
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                complete=True
            )

            for _ in range(randrange(1, 5)):
                price = randrange(10, 100)
                quantity = randrange(1, 5)
                OrderItem.objects.create(
                    order_id=order.id,
                    product_title=faker.name(),
                    price=price,
                    quantity=quantity,
                    admin_revenue=.9 * price * quantity,
                    ambassador_revenue=.1 * price * quantity
                )
