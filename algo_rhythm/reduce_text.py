from argparse import ArgumentTypeError

VALID_LETTERS = 'abc'
INVALID_TYPE_MESSAGE = 'Input must be a string.'
EMPTY_STRING_MESSAGE = 'Input must contain at least one character'
INVALID_STRING_MESSAGE = 'Input must contain only "A", "B" or "C" characters.'


def reduce_adjacent_characters(adjacent_characters: str) -> str:
    """
    Reduce two adjacent characters into a single one.

    Parameters
    ----------
    adjacent_characters : str
        Two characters (without spaces).

    Returns
    -------
    str
        Replacement character.

    """
    return set(VALID_LETTERS).difference(adjacent_characters).pop()


def get_reduced_list(text: str, reduced_list: list):
    """
    Get reduced strings list.

    Parameters
    ----------
    text : str
        Text to be reduced.
    reduced_list : list
        List to append reduced strings.

    """
    if len(set(text)) == 1:
        reduced_list.append(text)

    for index in range(len(text) - 1):
        adjacent_characters = text[index] + text[index + 1]
        if len(set(adjacent_characters)) == 2:
            get_reduced_list(
                text[:index] +
                reduce_adjacent_characters(adjacent_characters) +
                text[index + 2:],
                reduced_list
            )


def reduce_text_validator(text: str) -> str:
    """
    TODO docstring

    Raises
    ------
    TypeError
        If `text` is not a string.
    ValueError
        If `text` is an empty string.
    ValueError
        If `text` contain characters different from "A", "B" or "C".

    """
    if not isinstance(text, str):
        raise ArgumentTypeError(INVALID_TYPE_MESSAGE)

    if not text:
        raise ArgumentTypeError(EMPTY_STRING_MESSAGE)

    # To disallow upper case characters, comment next line
    text = text.casefold()

    if not set(text).issubset(VALID_LETTERS):
        raise ArgumentTypeError(INVALID_STRING_MESSAGE)

    return text


def reduce_text(text: str) -> int:
    """
    Return the smallest number of letters possible, following reduction method.

    Given a text (with only the letters "A", "B", or "C"), two different
    adjacent characters are replaced by the one different from both. This
    method is done repeatedly until the text cannot be further reduced.

    Parameters
    ----------
    text : str
        Text to be reduced.

    Returns
    -------
    int
        The number of letters at the end of the method.

    """
    reduced = []
    get_reduced_list(text, reduced)

    print(len(min(set(reduced), key=len)))
    return len(min(set(reduced), key=len))
    # TODO create printer
