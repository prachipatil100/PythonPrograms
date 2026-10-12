
import importlib.util

spec = importlib.util.spec_from_file_location(
    "vowels_consonants",
    "Code/11_vowels_consonants.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

count_vowels_consonants = module.count_vowels_consonants


def test_hello():
    assert count_vowels_consonants("Hello") == (2, 3)


def test_all_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert count_vowels_consonants("bcdf") == (0, 4)


def test_empty_string():
    assert count_vowels_consonants("") == (0, 0)


def test_mixed_text():
    assert count_vowels_consonants("Python 123") == (1, 5)
