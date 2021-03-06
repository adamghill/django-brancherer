from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import connection
from subprocess import call
from brancherer.base import DbNameMixin
from django.core.management import call_command
import os
import argparse
import ipdb


class Command(DbNameMixin, BaseCommand):
    help = 'Run another django command using you current git branch as the branch name'

    def add_arguments(self, parser):
        parser.add_argument('subcommand', nargs=argparse.REMAINDER)
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        subcommand = options['subcommand']
        settings.DATABASES['default']['NAME'] = self.full_branched_db_name
        call_command(*subcommand)
