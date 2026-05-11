import requests

def test_api():

    response = requests.get(
        "https://viacep.com.br/ws/01001000/json/"
    )

    assert response.status_code == 200