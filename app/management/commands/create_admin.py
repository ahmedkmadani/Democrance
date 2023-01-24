from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    """
    Command to seed db with admin user
    """

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("STARTED"))

        user = User.objects.filter(username="admin").first()
        if user:
            self.stdout.write(self.style.ERROR("USER IS ALREADY IN THE DB"))
        else:
            User.objects.create_superuser('admin', 'admin@mail.com', 'admin')

        self.stdout.write(self.style.NOTICE("FINISHED"))
