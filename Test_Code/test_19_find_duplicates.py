import importlib.util

spec = importlib.util.spec_from_file_location(
    "find_duplicates",
    "Code/19_find_duplicates.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates

def test_contains_duplicates():
    assert find_duplicates([1, 2, 3, 2, 1, 5]) == [1, 2]

def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_empty_input():
    assert find_duplicates([]) == []

def test_all_identical_duplicates():
    assert find_duplicates([7, 7, 7, 7]) == [7]

def test_string_duplicates():
    assert find_duplicates(["a", "b", "a"]) == ["a"]
