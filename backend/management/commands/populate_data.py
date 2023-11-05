# myapp/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from backend.models import Network  # Import your Network model

class Command(BaseCommand):
    help = 'Populate the Network model with hardcoded data'

    def handle(self, *args, **options):
        # Add your hardcoded data here
        Network.objects.create(name='Network A',status='Risk of failure')
        Network.objects.create(name='Network B',status='No risk of failure')
        Network.objects.create(name='Network C',status='Risk of failure')
        Network.objects.create(name='Network B',status='No risk of failure')

        self.stdout.write(self.style.SUCCESS('Successfully populated the Network model'))
