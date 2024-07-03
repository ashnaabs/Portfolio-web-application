# myapp/management/commands/delete_all_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Delete all registered users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        users_count = users.count()
        users.delete()
        self.stdout.write(f'Successfully deleted {users_count} users.')
