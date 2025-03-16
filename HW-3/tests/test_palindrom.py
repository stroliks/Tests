
from main import is_palindrom

import pytest

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             ("abba", True),
                            ("1221", True),
                            ("002200", True),
                            ("12345", False),
                            ("", False)
                          ])

def test_is_palindrom_positive(input_data, expected_result):
    assert is_palindrom(input_data) == expected_result


@pytest.mark.parametrize("input_data, expected_result",
                         [
                             (0, TypeError),
                             ([], TypeError),
                            (1256, TypeError),
                            (True, TypeError),
                          ])

def test_is_palindrom_negative(input_data, expected_result):
    with pytest.raises(expected_result):
        is_palindrom(input_data)

@pytest.mark.parametrize("input_data, expected_result",
                         [
                            ("", False),
                            ("f", True),
                            ("BfB", True),
                          ])

def test_is_palindrom_bound(input_data, expected_result):
    assert is_palindrom(input_data) == expected_result