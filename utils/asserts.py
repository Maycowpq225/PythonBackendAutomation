def assert_json(expected: dict, result: dict):
    differences = {}

    for key, expected_value in expected.items():
        if key not in result:
            differences[key] = {"error": "missing_key"}
            continue

        actual_value = result.get(key)

        if str(actual_value) != str(expected_value):
            differences[key] = {"error": "value_mismatch",}

    if differences:
        return False
    else:
        return True