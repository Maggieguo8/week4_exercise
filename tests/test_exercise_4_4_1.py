import pytest  # noqaF401
import numpy as np

"""Test the import and pattern,"""


def test_import_pattern():
    """Ensure we can import class Pattern."""
    from life.life import Pattern  # noqaF401


def test_pattern_grid():
    """Ensure the Pattern has correctly defined grid."""
    from life.life import Pattern, glider

    assert np.array_equal(Pattern(glider).grid, glider), \
        "Pattern.grid incorrectly defined"
