
import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome_string = module.is_palindrome_string


def test_palindrome_word():
    assert is_palindrome_string("madam") == True


def test_non_palindrome_word():
    assert is_palindrome_string("hello") == False


def test_uppercase_word():
    assert is_palindrome_string("Level") == True


def test_single_character():
    assert is_palindrome_string("a") == True


def test_empty_string():
    assert is_palindrome_string("") == True
