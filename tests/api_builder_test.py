def test_schema_from_api(api_response):

    assert isinstance(api_response, dict)
    assert isinstance(api_response["Data"], list)
