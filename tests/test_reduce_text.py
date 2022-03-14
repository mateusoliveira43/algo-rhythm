import pytest

from algo_rhythm.reduce_text import (
    EMPTY_STRING_MESSAGE,
    INVALID_STRING_MESSAGE,
    INVALID_TYPE_MESSAGE,
    get_reduced_list,
    reduce_adjacent_characters,
    reduce_text,
)

ADJACENT_CHARACTERS = [
    {'adjacent_characters': 'ab', 'replacement': 'c'},
    {'adjacent_characters': 'ba', 'replacement': 'c'},
    {'adjacent_characters': 'bc', 'replacement': 'a'},
    {'adjacent_characters': 'cb', 'replacement': 'a'},
    {'adjacent_characters': 'ac', 'replacement': 'b'},
    {'adjacent_characters': 'ca', 'replacement': 'b'},
]
VALID_INPUTS = [
    {'text': 'cab', 'reduced': 2},
    {'text': 'bcab', 'reduced': 1},
    {'text': 'abcabc', 'reduced': 2},
    {'text': 'cccc', 'reduced': 4},
    {'text': 'abc', 'reduced': 2},
    {'text': 'ABC', 'reduced': 2},
    {'text': 'a', 'reduced': 1},
    {'text': 'aaaaaa', 'reduced': 6},
    {'text': 'abbbbbc', 'reduced': 2},
    {'text': 'cba', 'reduced': 2},
    {'text': 'ba', 'reduced': 1},
    {'text': 'aBc', 'reduced': 2},
    {'text': 'AbC', 'reduced': 2},
    {'text': 'aaAAabbBCCaCc', 'reduced': 1},
]
INVALID_TYPE_INPUTS = [
    {'text': 1, 'message': INVALID_TYPE_MESSAGE},
    {'text': 1.1, 'message': INVALID_TYPE_MESSAGE},
    {'text': {}, 'message': INVALID_TYPE_MESSAGE},
    {'text': [], 'message': INVALID_TYPE_MESSAGE},
    {'text': set(), 'message': INVALID_TYPE_MESSAGE},
]
INVALID_VALUE_INPUTS = [
    {'text': '', 'message': EMPTY_STRING_MESSAGE},
    {'text': 'XYZ', 'message': INVALID_STRING_MESSAGE},
    {'text': 'xyz', 'message': INVALID_STRING_MESSAGE},
    {'text': '123', 'message': INVALID_STRING_MESSAGE},
    {'text': 'abd', 'message': INVALID_STRING_MESSAGE},
    {'text': 'a2c', 'message': INVALID_STRING_MESSAGE},
]


@pytest.mark.parametrize('scenario', ADJACENT_CHARACTERS)
def test_reduce_adjacent_characters(scenario):
    assert reduce_adjacent_characters(
        scenario['adjacent_characters']
    ) == scenario['replacement']


def test_get_reduced_list():
    test_list = []
    get_reduced_list('cab', test_list)
    assert test_list == ['bb', 'cc']


@pytest.mark.parametrize('scenario', VALID_INPUTS)
def test_reduce_text_valid_inputs(scenario):
    assert reduce_text(scenario['text']) == scenario['reduced']


@pytest.mark.parametrize('scenario', INVALID_TYPE_INPUTS)
def test_reduce_text_invalid_type_inputs(scenario):
    with pytest.raises(TypeError) as error:
        reduce_text(scenario['text'])
    assert scenario['message'] in str(error)


@pytest.mark.parametrize('scenario', INVALID_VALUE_INPUTS)
def test_reduce_text_invalid_value_inputs(scenario):
    with pytest.raises(ValueError) as error:
        reduce_text(scenario['text'])
    assert scenario['message'] in str(error)
