from django.urls import reverse


def test_list(client, messages):
    response = client.get(reverse('message-list'))
    data = response.json()

    assert len(messages) == len(data)


def test_list_params(client, messages):
    url = "{}?per_page=2&page=3".format(reverse('message-list'))
    response = client.get(url)
    data = response.json()

    assert len(data) == 2
