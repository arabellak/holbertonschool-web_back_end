#!/usr/bin/env python3
"""Unittests and Integration Tests
"""
import unittest
from nose.tools import assert_equal
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests access_nested_map function
    """

    @parameterized.expand([
        {"a": 1}, path=("a",),
        {"a": {"b": 2}}, path=("a",),
        {"a": {"b": 2}}, path=("a", "b")
    ])
    def test_access_nested_map(self, nestedMap, path, expected):
        """Test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nestedMap, path), expected)
