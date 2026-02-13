"""
test_utils.py

Unit tests for the `safe_name` function in beauti_tex.proj_builder.

The `safe_name` function sanitizes user-provided strings for use
as LaTeX project names or file/folder names by:

    - Replacing spaces with underscores
    - Replacing invalid characters with underscores
    - Ensuring the name is not empty
    - Removing or adjusting leading/trailing dots

These tests verify that various input strings are correctly
converted into safe, valid names.
"""

import pytest
from beauti_tex.proj_builder import safe_name

@pytest.mark.parametrize(
    "name,expected",
    [
        ("ValidName", "ValidName"),
        ("valid_name", "valid_name"),
        ("valid name", "valid_name"),
        ("valid<name>", "valid_name_"),
        ("valid:name", "valid_name"),
        ("", "empty"),
        ("validname.", "validname_"),
        (".validname", "validname"),
    ],
)
def test_valid_name(name, expected):
    """
    Test that `safe_name` correctly sanitizes various input strings.

    Args:
        name (str): Input string to sanitize.
        expected (str): Expected sanitized output.

    Asserts:
        The output of `safe_name(name)` matches `expected`.
    """
    assert safe_name(name) == expected