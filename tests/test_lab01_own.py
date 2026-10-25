import pytest
from basics import gc_percent, parse_counts

def test_gc_percent_boundary():
    """Boundary test: 100% GC content (no A or T)."""
    assert gc_percent(0, 50, 50, 0) == 100.0

def test_gc_percent_zero_total():
    """Zero-total case: all base counts zero should raise ValueError."""
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)


def test_parse_counts_invalid_input():
    """Invalid-input case: non-numeric tokens should raise ValueError."""
    with pytest.raises(ValueError):
        parse_counts("10 20 ten 30")