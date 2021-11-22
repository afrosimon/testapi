from datetime import datetime
import os
import csv
from django.core.management.base import BaseCommand


class Book(object):
    """
    As there are often multiple rows for a same book (a library having many copies)
    this class will serve as an abstraction, for instance to sum up the number
    of time the book was rented, over it's many copies
    """
    def __init__(self, row):
        self.title = row[8]
        self.author = row[10]
        self.editor = row[12]
        self.added_date = row[2]
        self.rental_count = int(row[3])

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise NotImplementedError

        return self.title == other.title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # there is often a "/" or ":" at the end of the titles
        try:
            if not value[-1].isalnum():
                self._title = value[:-1].strip()
            else:
                self._title = value.strip()
        except IndexError:
            self._title = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # there is often a comma at the end of the titles
        try:
            if not value[-1].isalnum():
                self._author = value[:-1].strip()
            else:
                self._author = value.strip()
        except IndexError:
            self._author = None

    @property
    def editor(self):
        return self._editor

    @editor.setter
    def editor(self, value):
        # there is often a comma at the end of the titles
        try:
            if not value[-1].isalnum():
                self._editor = value[:-1].strip()
            else:
                self._editor = value.strip()
        except IndexError:
            self._editor = None

    @property
    def rental_count(self):
        return self._rental_count

    @rental_count.setter
    def rental_count(self, value):
        self._rental_count = value

    @property
    def added_date(self):
        return self._added_date

    @added_date.setter
    def added_date(self, value):
        self._added_date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S-%f")


class Command(BaseCommand):
    help = "TBD"

    def add_arguments(self, parser):
        parser.add_argument(
            'source_file',
            type=str,
            help='Path of the data source'
        )

    def handle(self, *args, **options):
        source_file = options['source_file']

        if os.path.isfile(source_file):
            with open(source_file, 'r') as fp:
                former_book = None
                reader = csv.reader(fp)

                print('Beginning to import file')

                for i, row in enumerate(reader):
                    if i == 0:
                        continue

                    book = Book(row)

                    if former_book:
                        if book == former_book:
                            book.rental_count += former_book.rental_count
                        else:
                            print('{} *** {} *** {} *** {} *** {}'.format(
                                former_book.added_date,
                                former_book.title,
                                former_book.author,
                                former_book.rental_count,
                                former_book.editor
                            ))

                    former_book = book
        else:
            print('The source file provided does not exists')
