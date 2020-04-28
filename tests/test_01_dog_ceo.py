import pytest, requests, random


def test_1():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    parsed_data = response.json()
    assert parsed_data['status'] == 'success'


def test_2():
    response = requests.get('https://dog.ceo/api/breed/hound/images')
    parsed_data = response.json()['message']
    assert parsed_data[random.randint(1, 30)].endswith('.jpg')
    return parsed_data[:10]


def test_3(number_of_dogs):
    response = requests.get('https://dog.ceo/api/breeds/image/random/' + number_of_dogs)
    parsed_data = response.json()
    assert len(parsed_data['message']) == int(number_of_dogs)


@pytest.mark.parametrize('breed', ['african', 'labrador', 'terrier', 'wolfhound'])
def test_4(breed):
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    parsed_data = response.json()
    assert breed in parsed_data['message']


@pytest.fixture(params=test_2())
def params_for_test5(request):
    return request.param


def test_5(params_for_test5):
    url = params_for_test5
    assert requests.head(url).status_code == 200
