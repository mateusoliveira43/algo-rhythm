import pytest

from algo_rhythm.find_palindrome import (
    INVALID_STRING_MESSAGE,
    INVALID_TYPE_MESSAGE,
    find_palindrome,
    get_length_palindrome,
)

PALINDROMES = [
    {'text': 'aba', 'left': 1, 'right': 1, 'length': 3},
    {'text': 'abba', 'left': 1, 'right': 2, 'length': 4},
    {'text': 'abba', 'left': 3, 'right': 3, 'length': 1},
]
VALID_INPUTS = [
    {'text': 'abracecars', 'palindrome': 'racecar'},
    {'text': 'hellosannasmith', 'palindrome': 'sannas'},
    {'text': 'abcdefgg', 'palindrome': None},
    {'text': 'aa', 'palindrome': None},
    {'text': 'aaaa', 'palindrome': 'aaaa'},
]
INVALID_TYPE_INPUTS = [
    {'text': 1, 'message': INVALID_TYPE_MESSAGE},
    {'text': 1.1, 'message': INVALID_TYPE_MESSAGE},
    {'text': {}, 'message': INVALID_TYPE_MESSAGE},
    {'text': [], 'message': INVALID_TYPE_MESSAGE},
    {'text': set(), 'message': INVALID_TYPE_MESSAGE},
]
INVALID_VALUE_INPUTS = [
    {'text': '', 'message': INVALID_STRING_MESSAGE},
    {'text': '1', 'message': INVALID_STRING_MESSAGE},
    {'text': 'XYZ', 'message': INVALID_STRING_MESSAGE},
    {'text': '123', 'message': INVALID_STRING_MESSAGE},
    {'text': 'a2c', 'message': INVALID_STRING_MESSAGE},
    {'text': 'a.', 'message': INVALID_STRING_MESSAGE},
    {'text': 'a?', 'message': INVALID_STRING_MESSAGE},
    {'text': 'a*', 'message': INVALID_STRING_MESSAGE},
]


@pytest.mark.parametrize('scenario', PALINDROMES)
def test_get_length_palindrome(scenario):
    assert get_length_palindrome(
        scenario['text'], scenario['left'], scenario['right']
    ) == scenario['length']


@pytest.mark.parametrize('scenario', VALID_INPUTS)
def test_find_palindrome_valid_inputs(scenario):
    assert find_palindrome(
        scenario['text']
    ) == scenario['palindrome']


@pytest.mark.parametrize('scenario', INVALID_TYPE_INPUTS)
def test_find_palindrome_invalid_type_inputs(scenario):
    with pytest.raises(TypeError) as error:
        find_palindrome(scenario['text'])
    assert scenario['message'] in str(error)


@pytest.mark.parametrize('scenario', INVALID_VALUE_INPUTS)
def test_find_palindrome_invalid_value_inputs(scenario):
    with pytest.raises(ValueError) as error:
        find_palindrome(scenario['text'])
    assert scenario['message'] in str(error)
