
import importlib.util

spec = importlib.util.spec_from_file_location(
    "common_elements",
    "Code/17_common_elements.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

common_elements = module.common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4], [2, 3, 5, 6]) == [2, 3]


def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []


def test_same_lists():
    assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_duplicate_elements():
    assert common_elements([1, 2, 2, 3], [2, 2, 3]) == [2, 3]


def test_empty_list():
    assert common_elements([], [1, 2, 3]) == []
