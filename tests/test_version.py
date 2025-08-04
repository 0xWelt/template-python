"""Test version output."""

import template_python


def test_version_output():
    """Test that version can be accessed and printed."""
    print(f'Version: {template_python.__version__}')
    assert template_python.__version__ is not None
