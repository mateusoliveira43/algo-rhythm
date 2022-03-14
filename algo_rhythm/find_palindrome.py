from math import floor
from typing import Optional

MINIMUM_LENGTH = 3
INVALID_TYPE_MESSAGE = 'Input must be a string.'
INVALID_STRING_MESSAGE = (
    'Input must contain at least one, and only, lowercase alphabetic '
    'characters.'
)


def get_length_palindrome(text: str, left: int, right: int) -> int:
    """
    Get length of longest palindrome inside text, given right and left indexes.

    Get the length of the longest palindrome of a given text, which begins with
    the character at the left index of the string and ends with the character
    at the right index of the string.

    Parameters
    ----------
    text : str
        Text to get palindrome from.
    left : int
        The left index of the string
    right : int
        The right index of the string

    Returns
    -------
    int
        Length of the longest palindrome.

    """
    while left >= 0 and right < len(text) and text[left] == text[right]:
        left -= 1
        right += 1

    return right - left - 1


def find_palindrome(text: str) -> Optional[str]:
    """
    Return the longest palindrome inside a given a text.

    Given an input string, returns the longest palindromic substring of the
    string possible, which means the longest substring of the string which is
    read the same forwards as it is backwards.

    Parameters
    ----------
    text : str
        Text to get longest palindromic substring.

    Returns
    -------
    Optional[str]
        Longest palindromic substring from `text`, if it is has more than two
        characters; None, otherwise.

    Raises
    ------
    TypeError
        If `text` is not a string.
    ValueError
        If `text` contain characters different lowercase alphabetic
        characters or is an empty string.

    """
    # TODO create validator
    if not isinstance(text, str):
        raise TypeError(INVALID_TYPE_MESSAGE)

    if not (text.isalpha() and text.islower()):
        raise ValueError(INVALID_STRING_MESSAGE)

    text_length = len(text)
    if text_length < MINIMUM_LENGTH:
        return None

    start = end = 0
    for index in range(text_length):
        length_odd = get_length_palindrome(text, index, index)
        length_even = get_length_palindrome(text, index, index + 1)
        length = max(length_odd, length_even)
        if length > end - start:
            start = index - floor((length - 1) / 2)
            end = index + floor(length / 2)

    if end - start < MINIMUM_LENGTH - 1:
        return None
    print(text[start:end + 1])
    return text[start:end + 1]
    # TODO create printer
