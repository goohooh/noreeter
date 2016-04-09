from django.core.management import BaseCommand

from towns.models import Town


class Command(BaseCommand):

    def handle(self, **options):
        self.stdout.write('load address data...')

        address_file = open('/Users/seongpil/Desktop/address.txt', 'r')

        lines = address_file.readlines()
        address_file.close()

        for line in lines:
            split_line = line.split(' ')

            Town.objects.create(
                full_address=line.replace('\n', ''),
                state=split_line[0],
                city=split_line[1],
                town_name=split_line[2].replace('\n', ''),
            )
