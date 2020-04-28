import pytest, requests


def test_addoption_params(url_param):
    # print(url_param['url'])
    # print(url_param['status_code'])
    response = requests.head(url_param['url'])
    print(response)
    assert response.status_code == url_param['status_code']
