
import importlib.util

spec = importlib.util.spec_from_file_location(
    "word_frequency",
    "Code/20_word_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

word_frequency = module.word_frequency


def test_repeated_words():
    assert word_frequency("apple mango apple") == {
        "apple": 2,
        "mango": 1
    }


def test_single_word():
    assert word_frequency("hello") == {"hello": 1}


def test_empty_string():
    assert word_frequency("") == {}


def test_uppercase_words():
    assert word_frequency("Apple apple MANGO") == {
        "apple": 2,
        "mango": 1
    }


def test_multiple_repeated_words():
    assert word_frequency("cat dog cat dog cat") == {
        "cat": 3,
        "dog": 2
    }
