#!/usr/bin/env python3
import config
import sys
import permutation
import find_palindrome
import reduce_text

COMMANDS = {
    permutation.permutation.__name__: permutation.permutation,
    find_palindrome.find_palindrome.__name__: find_palindrome.find_palindrome,
    reduce_text.reduce_text.__name__: reduce_text.reduce_text,
}

parser = config.configured_parser('algo-rhythms')

subparser = parser.add_subparsers(
    dest='command',
    metavar='[COMMAND]',
    title='Commands',
    prog=sys.argv[0]
)
permutation_command = subparser.add_parser(
    permutation.permutation.__name__,
    help=(
        'Get the permutations of a text and the numbers of permutations and '
        'unique permutations it has.'
    )
)
permutation_command.add_argument(
    'text',
    type=str,
    help='Text to get permutation information.'
)

palindrome_command = subparser.add_parser(
    find_palindrome.find_palindrome.__name__,
    help=(
        'Return the longest palindrome inside a given a text.'
        '\n'
        'Given an input string, returns the longest palindromic substring of the'
        'string possible, which means the longest substring of the string which is'
        'read the same forwards as it is backwards.'
    )
)
palindrome_command.add_argument(
    'text',
    type=str,
    help='Text to get longest palindromic substring.'
)

reduce_command = subparser.add_parser(
    reduce_text.reduce_text.__name__,
    help=(
        'Return the smallest number of letters possible, following reduction method.'
        '\n'
        'Given a text (with only the letters "A", "B", or "C"), two different'
        'adjacent characters are replaced by the one different from both. This'
        'method is done repeatedly until the text cannot be further reduce'
    )
)
reduce_command.add_argument(
    'text',
    type=reduce_text.reduce_text_validator,
    help='Text to be reduced.'
)


def main():
    """Run script on user call."""
    args = config.initialize_parser(parser)
    if args.command:
        COMMANDS.get(args.command)(args.text)


if __name__ == '__main__':
    main()
