import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_string",
    "Code/12_reverse_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_string  = module.reverse_string

def test_reverse_word():
    assert reverse_string("hello") == "olleh"

def test_single_character():
    assert reverse_string("a") == "a"

def test_empty_string():
    assert reverse_string("") == ""

def test_reverse_sentence_word():
    assert reverse_string("Python") == "nohtyP"

def test_reverse_with_number():
    assert reverse_string("abc 123") == "321 cba"