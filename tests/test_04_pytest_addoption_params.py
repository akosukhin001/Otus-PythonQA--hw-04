import pytest, requests


def test_addoption_params(url_param):
    # print(url_param)
    url, arg_status_code = url_param
    print(url, arg_status_code)
    response = requests.head(url)
    print(response)
    assert response.status_code == arg_status_code
