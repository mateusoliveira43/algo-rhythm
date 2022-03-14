PERMUTATIONS = []


def get_permutations(text: str, permutation: str = ''):
    """
    Get the permutations of a given text.

    Parameters
    ----------
    text : str
        Text to get the permutations of.
    permutation : str, optional
        Auxiliary variable used to build the permutations, by default an empty
        string.

    """
    if not text:
        PERMUTATIONS.append(permutation)
    else:
        for index, letter in enumerate(text):
            get_permutations(
                text[:index] + text[index+1:], permutation + letter
            )
            # TODO which is faster?


def permutation(text):
    # TODO add tests
    get_permutations(text)
    # TODO transform  this part in a function
    print(
        f'The text {text} has {len(PERMUTATIONS)} permutations '
        f'({len(set(PERMUTATIONS))} being unique), which are:'
    )
    for permutation in PERMUTATIONS:
        print(' ', permutation)
