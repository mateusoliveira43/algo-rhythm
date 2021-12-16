#!/usr/bin/env python3
import config

DESCRIPTION = (
    'Get the permutations of a text and the numbers of permutations and '
    'unique permutations it has.'
)
PERMUTATIONS = []

parser = config.configured_parser(DESCRIPTION)

parser.add_argument(
    'text',
    type=str,
    help='Text to get permutation information.'
)


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
        for index in range(len(text)):
            get_permutations(
                text[:index] + text[index+1:], permutation + text[index]
            )


def main():
    """Run script on user call."""
    args = config.initialize_parser(parser)
    get_permutations(args.text)
    # TODO tranform  this part in a function
    print(
        f'The text {args.text} has {len(PERMUTATIONS)} permutations '
        f'({len(set(PERMUTATIONS))} beeing unique), which are:'
    )
    for permutation in PERMUTATIONS:
        print(' ', permutation)


if __name__ == '__main__':
    main()
