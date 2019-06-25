import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def client(db):
    # NOTE: We could also declare that object in every test, but with this fixture
    # since we include the DB fixture we don't need to mark every test with the DB decorator
    return APIClient()
