import pytest
from tests.services import providerService

@pytest.mark.provider
def test_create_user():
    responseJson = providerService.createUser()
    assert responseJson['status'] == 201
    assert responseJson['message'] == 'Provider Registered.'