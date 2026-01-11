"""Tests for myproj.builtins_cheatsheet module."""

from myproj.builtins_cheatsheet import (
    get_builtins_list,
    group_builtins_by_initial,
    format_builtins_cheatsheet,
    get_builtins_count,
    write_cheatsheet,
)


def test_get_builtins_list():
    """Test that get_builtins_list returns a non-empty sorted list."""
    builtins_list = get_builtins_list()
    assert isinstance(builtins_list, list)
    assert len(builtins_list) > 0
    assert builtins_list == sorted(builtins_list)
    # Check that no private names are included
    assert not any(name.startswith('_') for name in builtins_list)


def test_get_builtins_list_contains_common_functions():
    """Test that common builtins are in the list."""
    builtins_list = get_builtins_list()
    common_builtins = ['len', 'str', 'int', 'list', 'dict', 'print', 'range']
    for builtin in common_builtins:
        assert builtin in builtins_list


def test_group_builtins_by_initial():
    """Test that grouping by initial letter works correctly."""
    grouped = group_builtins_by_initial()
    assert isinstance(grouped, dict)
    assert len(grouped) > 0
    # Check that all keys are uppercase letters
    assert all(len(k) == 1 and k.isalpha() and k.isupper() for k in grouped.keys())
    # Check that all values are lists
    assert all(isinstance(v, list) for v in grouped.values())


def test_group_builtins_by_initial_completeness():
    """Test that all builtins are in the grouped dictionary."""
    builtins_list = get_builtins_list()
    grouped = group_builtins_by_initial()
    
    all_grouped = []
    for names in grouped.values():
        all_grouped.extend(names)
    
    assert sorted(all_grouped) == builtins_list


def test_write_cheatsheet_writes_file(tmp_path):
    """Test that write_cheatsheet writes a file with expected content."""
    out = tmp_path / "cheatsheet.txt"
    # use the real builtins list for this test
    path = write_cheatsheet(out)
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    # It should contain at least one header letter and the total count
    assert "A" in text
    assert f"Total builtins: {get_builtins_count()}" in text


def test_group_builtins_by_initial_letters():
    """Test that builtins are grouped under their correct initial letter."""
    grouped = group_builtins_by_initial()
    
    for letter, names in grouped.items():
        for name in names:
            assert name[0].upper() == letter


def test_format_builtins_cheatsheet():
    """Test that cheatsheet formatting returns a non-empty string."""
    cheatsheet = format_builtins_cheatsheet()
    assert isinstance(cheatsheet, str)
    assert len(cheatsheet) > 0
    # Check that it contains separator lines
    assert '=' in cheatsheet
    # Check that it contains some common builtins
    assert 'len' in cheatsheet
    assert 'print' in cheatsheet


def test_format_builtins_cheatsheet_contains_all_builtins():
    """Test that all builtins appear in the formatted cheatsheet."""
    builtins_list = get_builtins_list()
    cheatsheet = format_builtins_cheatsheet()
    
    for builtin in builtins_list:
        assert builtin in cheatsheet


def test_get_builtins_count():
    """Test that the count matches the list length."""
    builtins_list = get_builtins_list()
    count = get_builtins_count()
    assert count == len(builtins_list)
    assert count > 0
