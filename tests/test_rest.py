import pytest
from .test_sql_app import client


def test_create_image():
    response = client.get('/get_last_images')
    assert response.status_code == 200
    assert response.json() == []
