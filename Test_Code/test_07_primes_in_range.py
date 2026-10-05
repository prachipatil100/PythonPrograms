import importlib.util

spec = importlib.util.spec_from_file_location(
    "primes_in_range",
    "Code/07_primes_in_range.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

primes_in_range = module.primes_in_range

def test_standard_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]

def test_empty_range():
    assert primes_in_range(8, 10) == []

def test_single_prime():
    assert primes_in_range(11, 12) == [11]

def test_invalid_range():
    assert primes_in_range(20, 10) == []

def test_negative_range():
    assert primes_in_range(-5, 5) == [2, 3, 5]
