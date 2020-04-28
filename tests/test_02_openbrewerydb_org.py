import requests, pytest
from jsonschema import validate


def test_1(city):
    url = 'https://api.openbrewerydb.org/breweries?by_city=' + city
    print(url)
    assert requests.get(url).ok


def test_2(fixture_for_openbrewery_tests):
    response = requests.get('https://api.openbrewerydb.org/breweries')
    print(response.json()[fixture_for_openbrewery_tests]["country"])
    assert response.json()[fixture_for_openbrewery_tests]["country"] == "United States"


@pytest.mark.parametrize('brw_type', ['micro', 'regional', 'brewpub', 'large',
                                      'planning', 'bar', 'contract', 'proprietor'])
def test_3(brw_type):
    assert requests.get('https://api.openbrewerydb.org/breweries?by_type=' + brw_type).json() != []


def test_4(fixture_for_openbrewery_tests):
    response = requests.get('https://api.openbrewerydb.org/breweries')
    print(response.json()[fixture_for_openbrewery_tests]["id"])
    assert isinstance(response.json()[fixture_for_openbrewery_tests]["id"], int)


@pytest.mark.parametrize('index', range(10))
def test_5_json_schema(index):
    response = requests.get('https://api.openbrewerydb.org/breweries')
    print(response.json()[index])
    schema = {
        "type": "object",
        "properties":
            {
                "id": {"type": "number"},
                # "id": {"type":"string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": "string"},
                "latitude": {"type": "string"},
                "phone": {"type": "string"},
                "website_url": {"type": "string"},
                "updated_at": {"type": "string"},
                "tag_list": {"type": "array"},
            },
        "required": ["id", "name", "city", "state", "postal_code", "country"]
    }
    validate(instance=response.json()[index], schema=schema)
