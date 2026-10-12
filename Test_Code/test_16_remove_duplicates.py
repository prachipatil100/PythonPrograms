
import importlib.util

spec = importlib.util.spec_from_file_location(
    "remove_duplicates",
    "Code/16_remove_duplicates.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

remove_duplicates = module.remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_all_duplicates():
    assert remove_duplicates([5, 5, 5]) == [5]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_preserve_order():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
