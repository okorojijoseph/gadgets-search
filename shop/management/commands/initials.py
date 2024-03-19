from typing import List
from django.conf import settings
from django.core.management.base import BaseCommand
import logging

from .mappings import CLIENT_TEST_DATA, PRODUCTS_TEST_DATA, SUPERUSER_TEST_DATA
from shop.models import Product, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CreateData(object):
    def __init__(self):
        user = self.create_superuser()
        self.create_client()
        self.create_products(user)

    def create_superuser(self) -> User:
        superuser, created = User.objects.get_or_create(
            email=settings.FIRST_SUPERUSER_EMAIL, defaults=SUPERUSER_TEST_DATA
        )
        if created:
            superuser.set_password(settings.FIRST_SUPERUSER_PASSWORD)
            superuser.save()
        return superuser

    def create_client(self) -> User:
        client, created = User.objects.get_or_create(
            email=settings.FIRST_CLIENT_EMAIL, defaults=CLIENT_TEST_DATA
        )
        if created:
            client.set_password(settings.FIRST_CLIENT_PASSWORD)
            client.save()
        return client

    def create_products(self, user) -> List[Product]:
        products_to_create = [Product(user=user, **p) for p in PRODUCTS_TEST_DATA]
        Product.objects.bulk_create(products_to_create)


def init() -> None:
    CreateData()


class Command(BaseCommand):
    def handle(self, **options) -> None:
        logger.info("Creating initial data")
        init()
        logger.info("Initial data created")
