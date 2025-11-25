import pytest
from tests.services import provider_service
import json
from tests.db import provider_table
from utils.asserts import assert_json

@pytest.mark.provider
def test_create_user():
    request = provider_service.create_user()
    request_payload = json.loads(request.request.body)
    del request_payload["password"]
    user_data_from_db = provider_table.get_provider_by_email(request_payload['email'])
    assert request.json()['status'] == 201
    assert request.json()['message'] == 'Provider Registered.'
    assert assert_json(request_payload, user_data_from_db)

