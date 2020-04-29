import pytest


@pytest.fixture(params=['3', '4', '5'])
def number_of_dogs(request):
    return request.param


@pytest.fixture(params=['san_diego', 'Birmingham', 'Huntsville', 'Wasilla'])
def city(request):
    return request.param


@pytest.fixture(params=range(20))
def fixture_for_openbrewery_tests(request):
    return request.param


@pytest.fixture(params=range(5))
def fixture_for_jsonplaceholder_tests(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption('--url', help='choose url to test', default='https://ya.ru')
    parser.addoption('--status_code', type=int, help='http status code', default=200)


@pytest.fixture
def url_param(request):
    url = request.config.getoption('--url')
    status_code = request.config.getoption('--status_code')
    # return {'url': url, 'status_code': status_code}  # Вариант передачи аргументов в тестовую ф-ю через словарь.
    return url, status_code
