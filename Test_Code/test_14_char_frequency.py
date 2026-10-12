import importlib.util

spec = importlib.util.spec_from_file_location(
    "char_frequency",
    "Code/14_char_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

char_frequency = module.char_frequency

def test_frequency_repeats():
    assert char_frequency("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}

def test_frequency_unique():
    assert char_frequency("cat") == {'c': 1, 'a': 1, 't': 1}

def test_frequency_empty():
    assert char_frequency("") == {}

def test_frequency_spaces():
    assert char_frequency("a a") == {'a': 2, ' ': 1}

def test_frequency_case():
    assert char_frequency("Aa") == {'A': 1, 'a': 1}
