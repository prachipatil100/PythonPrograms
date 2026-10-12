
import importlib.util

spec = importlib.util.spec_from_file_location(
    "missing_number",
    "Code/18_missing_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_missing_number = module.find_missing_number


def test_missing_middle_number():
    assert find_missing_number([0, 1, 3, 4]) == 2


def test_missing_zero():
    assert find_missing_number([1, 2, 3]) == 0


def test_missing_last_number():
    assert find_missing_number([0, 1, 2, 3]) == 4


def test_single_number_list():
    assert find_missing_number([0]) == 1


def test_unsorted_list():
    assert find_missing_number([4, 0, 3, 1]) == 2
