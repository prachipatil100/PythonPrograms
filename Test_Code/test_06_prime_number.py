import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/06_prime_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Is_prime = module.Is_prime

def test_prime_number():
    assert Is_prime(7) == True

def test_non_prime_number():
    assert Is_prime(8) == False

def test_two():
    assert Is_prime(2) == True

def test_one():
    assert Is_prime(1) == False

def test_zero():
    assert Is_prime(0) == False