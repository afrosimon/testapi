import pytest
from django.contrib.auth.models import User
from message.models import Message


@pytest.fixture
def first_user():
    u = User(
        username='Alice',
        email='alice@asd.com'
    )
    u.save()

    return u

@pytest.fixture
def second_user():
    u = User(
        username='Bob',
        email='bob@asd.com'
    )
    u.save()

    return u

@pytest.fixture
def messages(first_user, second_user):
    messages = []

    for _ in range(0, 10):
        message = Message(
            sender=first_user,
            recipient=second_user,
            content='test'
        )
        message.save()

        messages.append(message)

    return messages
