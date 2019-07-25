from uuid import uuid4
from random import randrange
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from message.models import Message


DEFAULT_NB_MESSAGES = 100
DEFAULT_NB_USERS = 10
DUMMY_CONTENTS = [
    'Maybe yes, maybe no',
    'You would think so but you are sorely mistaken',
    'Dans le fond, pourquoi pas buddy',
    'Peut-être mais je pense pas sérieux',
    'I wouldn\'t bet on that',
    'Интегрировал значит Денис Алису на стрим',
    'Найс повтор... думал дальше стрим пошёл =/',
    'bilgisayarım mario kaldırıyo Pog',
    '就一直要他深一點，很厲害這樣',
    '超沒常識',
    'ジンのEっていつ出番が来るんだろう',
    'パイクがお仕置き食らうのは来週',
    'USA A PASSIVA COM O E QUE DA SLOW',
    'metade dos cara falando pra desviar, tomariam tudo',
]
DUMMY_USERNAMES = [
    'yadayada',
    'bro123',
    'asd',
    'potato',
    'fakeusername',
    'jaja456',
    'donaldo11',
    'leet666',
    'pomme_de_terre',
    'saitama',
    'kekekekekekeke',
]


class Command(BaseCommand):
    help = "Generate a number of message objects"

    def add_arguments(self, parser):
        parser.add_argument(
            '--messages',
            type=int,
            help='Number of messages to generate, default is 100'
        )
        parser.add_argument(
            '--users',
            type=int,
            help='Number of users to create and associate with each message, default is 10'
        )

    def handle(self, *args, **options):
        if options['messages']:
            nb_messages = options['messages']
        else:
            nb_messages = DEFAULT_NB_MESSAGES

        if options['users']:
            nb_users = options['users']
        else:
            nb_users = DEFAULT_NB_USERS

        users = []

        print("Starting the generation...")

        for _ in range(0, nb_users):
            username = "{}-{}".format(
                DUMMY_USERNAMES[randrange(0, len(DUMMY_USERNAMES))],
                uuid4()
            )
            user = User(
                username=username,
                email='{}@asd.com'.format(username)
            )
            user.save()

            users.append(user)

        print("Created {} users.".format(nb_users))

        for _ in range(0, nb_messages):
            message = Message(
                sender=users[randrange(0, len(users))],
                recipient=users[randrange(0, len(users))],
                content=DUMMY_CONTENTS[randrange(0, len(DUMMY_CONTENTS))]
            )
            message.save()

        print("Created {} messages. Success!".format(nb_messages))
