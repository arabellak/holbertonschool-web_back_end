#!/usr/bin/env python3
"""Unittests and Integration Tests
"""
import unittest
from unittest import mock
from nose.tools import assert_equal
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests access_nested_map function
    """

    @parameterized.expand([
        {"a": 1}, path=("a",),
        {"a": {"b": 2}}, path=("a",),
        {"a": {"b": 2}}, path=("a", "b")
    ])
    def test_access_nested_map(self, nestedMap, path, expected):
        """
            Test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nestedMap, path), expected)

    @parameterized.expand([
        {}, path=("a",),
        {"a": 1}, path=("a", "b")
    ])
    def test_access_nested_map_exception(self, nestedMap, path, expected):
        """
            Tests that a KeyError is raise with the above inputs
        """
        with self.assertRaises(expected):
            access_nested_map(nestedMap, path)

    class TestGetJson(unittest.TestCase):
        """
            Tests that returns the expected result
        """
        @parameterized.expand([
            "http://example.com", test_payload={"payload": True},
            "http://holberton.io", test_payload={"payload": False}
        ])
        def test_get_json(self, testPayload, testUrl):
            """
                Test get_json
            """
            m = mock.Mock()
            m.json.return_value = testPayload

            with mock.patch('request.get', return_value=m):
                mock_request = get_json(testUrl)
                m.json.assert_called_once()
                self.assertEqual(mock_request, testPayload)

    class TestMemoize(unittest.TestCase):
        """
            Tests memoize
        """
        def test_memoize():
            """
                Memoize test
            """
            class TestClass:

                def a_method(self):
                    return 42

                @memoize
                def a_property(self):
                    return self.a_method()

            with patch.object(TestClass, "a_method") as mock_a:
                mock_a.return_value = True
                test = TestClass()
                test.a_property
                test.a_property
                mock_a.assert_called_once()
