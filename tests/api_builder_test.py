def test_schema_from_api(api_response_data):

    assert isinstance(api_response_data, dict)
    assert isinstance(api_response_data["Data"], list)
