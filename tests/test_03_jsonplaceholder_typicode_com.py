import requests, pytest, random
from jsonschema import validate


def test_1():
    response = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
    index = random.randrange(1, 10)
    print('\nIndex is: ', index)
    # print(response.json()[index])
    assert response.json()[index]['id'] < 10


def test_2():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.ok


@pytest.mark.parametrize('param', [{'userId': 1}, {'userId': 2}, {'userId': 3}])
def test_3(fixture_for_jsonplaceholder_tests, param):
    param_response = requests.get('https://jsonplaceholder.typicode.com/posts/', params=param)
    print(param['userId'])
    assert param_response.json()[fixture_for_jsonplaceholder_tests]['userId'] == param['userId']


def test_4():
    json_data_to_post = {'userId': 11, 'title': 'Red Hot Chili Peppers', 'body': 'Californication (1998—2001)'}
    headers = {"Content-type": 'application/json; charset=utf-8'}

    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=json_data_to_post, headers=headers)
    # print('\n-----\n\n response: ', response.status_code)
    # print('\n-----\n\n response.headers: ', response.headers)
    # print('\n-----\n\n response.request: ', response.request)
    # print('\n-----\n\n response.text: ', response.text)
    print('\n-----\n\n title: ', response.json()['title'])
    assert response.json()['title'] == json_data_to_post['title']


@pytest.mark.parametrize('index', range(100))
def test_5_json_schema(index):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(response.json()[index])
    schema = {
        "type": "object",
        "properties":
            {
                "userId": {"type": "number"},
                # "userId": {"type": "string"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "body": {"type": "string"},
            },
        "required": ["userId", "id", "title", "body"]
    }
    validate(instance=response.json()[index], schema=schema)
