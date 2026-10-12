import importlib.util

spec = importlib.util.spec_from_file_location(
    "second_largest",
    "Code/15_second_largest.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

get_second_largest = module.get_second_largest

def test_standard_list():
    assert get_second_largest([1, 2, 3, 4, 5]) == 4

def test_list_with_duplicates():
    assert get_second_largest([10, 20, 20, 15]) == 15

def test_insufficient_elements():
    assert get_second_largest([7]) is None

def test_all_identical():
    assert get_second_largest([5, 5, 5]) is None

def test_negative_elements():
    assert get_second_largest([-10, -5, -2, -20]) == -5
