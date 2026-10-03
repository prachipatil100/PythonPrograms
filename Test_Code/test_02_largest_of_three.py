import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest_of_three",
    "Code/02_largest_of_three.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_largest = module.find_largest

def test_largest_third():
    assert find_largest(1, 2, 3) == 3

def test_largest_second():
    assert find_largest(5, 20, 10) == 20

def test_largest_first():
    assert find_largest(50, 12, 34) == 50

def test_all_negative():
    assert find_largest(-10, -5, -20) == -5

def test_all_equal():
    assert find_largest(7, 7, 7) == 7
if __name__ =="__main__":
    test_largest_third()
    test_largest_second()
    test_largest_first()
    test_all_negative()
    test_all_equal()
    print("All test cases passed.")