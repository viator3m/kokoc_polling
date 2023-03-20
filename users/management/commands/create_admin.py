from django.conf import settings as conf
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username=conf.DJ_USER).exists():
            User.objects.create_superuser(username=conf.DJ_USER,
                                          email=conf.DJ_EMAIL,
                                          password=conf.DJ_PWD,)
