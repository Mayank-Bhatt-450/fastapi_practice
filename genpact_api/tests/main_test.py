import pytest
from genpact_api import main
from fastapi.testclient import TestClient
import fastapi

@pytest.mark.vcr(
    match_on=['url'],
    record_mode='once',
    filter_header=["Authorization"]

)
def test_cities_search_by_prefix():
    # Arrange
    city_prefix = 'Z'
    expected_output=["Zawiya","Zlitan","Zuwarah"]
    # Act
    response = main.get_cities(  city_prefix=city_prefix  )

    #arrange
    assert expected_output==response['cities']

@pytest.mark.vcr(
    match_on=['url'],
    record_mode='once',
    filter_header=["Authorization"]

)
def test_cities_search_by_prefix_response():
    # Arrange
    client = TestClient(main.app)
    city_prefix = 'Z'
    expected_output=["Zawiya","Zlitan","Zuwarah"]
    # Act
    response = client.get(f"/cities/{city_prefix}")
   
    #arrange
    assert expected_output==response.json()['cities']
    assert response.status_code == fastapi.status.HTTP_200_OK
    