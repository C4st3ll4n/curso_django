from django.test import Client


def test_status_code(client: Client):
    rest = client.get("/")
    assert rest.status_code == 200
