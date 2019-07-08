from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from register.forms import RegisterForm

from faker import Faker

# from faker.providers import internet
fake = Faker()


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')


    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string, email=fake.free_email(),password='123456')
