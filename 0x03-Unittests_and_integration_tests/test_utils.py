#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test utils.access_nested_map.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
        self,
        nested_map,
        path,
        expected_exception_message
    ):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Tests the memoize function
    """
    def test_memoize(self):
        class TestClass():
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, 'a_method', return_value=42) as mock_a_method:
            result_1 = test_obj.a_property
            result_2 = test_obj.a_property
            mock_a_method.assert_called_once()
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)


if __name__ == "__main__":
    unittest.main()
