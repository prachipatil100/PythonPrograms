import importlib.util

spec = importlib.util.spec_from_file_location(
    "fibonacci_series",
    "Code/05_fibonacci_series.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

generate_fibonacci = module.generate_fibonacci

def test_fib_zero():
    assert generate_fibonacci(0) == []

def test_fib_one():
    assert generate_fibonacci(1) == [0]

def test_fib_two():
    assert generate_fibonacci(2) == [0, 1]

def test_fib_five():
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]

def test_fib_negative():
    assert generate_fibonacci(-3) == []
