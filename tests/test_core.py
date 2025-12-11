"""Tests for myproj.core module."""

import pytest
from myproj.core import greet


def test_greet_world():
    """Test that greet returns the expected greeting."""
    assert greet("World") == "Hello, World!"


def test_greet_custom_name():
    """Test greet with a custom name."""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_string():
    """Test greet with an empty string."""
    assert greet("") == "Hello, !"
