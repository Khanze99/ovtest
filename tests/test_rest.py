import os

from .test_sql_app import client
from ov.service import image2base64


def test_post_image():
    path = 'tests/images/'
    images = os.listdir(path)

    for image in images:
        base64 = image2base64(path + image)
        response = client.post('/ovision/negative_image/', json={"name": image.split('.')[0], "image": base64})
        assert response.status_code == 200
        assert type(response.json()['negative_image']) is str


def test_get_image():
    response = client.get('/ovision/get_last_images')
    assert len(response.json()) == 3
    assert response.status_code == 200
