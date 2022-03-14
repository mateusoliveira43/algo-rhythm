import argparse
import sys

# TODO git submodule?
USAGE_PREFIX = 'Usage:\n  [python|python3] '
EPILOG = 'Algo-rhythm \U0001F3B5'
POSITIONALS_TITLE = 'Required options'
OPTIONALS_TITLE = 'Options'
HELP_MESSAGE = "Show script's help message."


class CustomFormatter(argparse.HelpFormatter):
    """
    Custom formatter for argparse's argument parser.

    Methods
    -------
    _format_usage(self, usage, actions, groups, prefix)
        Formats prefix of usage section.

    _format_action(self, action)
        Removes subparser's metavar when listing its parsers.

    _format_action_invocation(self, action)
        Adds metavar only once to arguments.

    """
    def __init__(self, *args, **kwargs):
        """Call super class init's."""
        super().__init__(*args, **kwargs)

    def _format_usage(self, usage, actions, groups, prefix):
        return super()._format_usage(
            usage, actions, groups, USAGE_PREFIX
        )

    def _format_action(self, action):
        parts = super()._format_action(action)
        if action.nargs == argparse.PARSER:
            line_break = '\n'
            parts = line_break.join(parts.split(line_break)[1:])
        return parts

    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        metavar = self._format_args(
            action, self._get_default_metavar_for_optional(action)
        )
        comma = ', '
        return f'{comma.join(action.option_strings)} {metavar}'


def configured_parser(description: str) -> argparse.ArgumentParser:
    """
    Create configured parser to create script.

    Parameters
    ----------
    description : str
        Description of the script.

    Returns
    -------
    ArgumentParser
        Configured argparse's parser.

    """
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description=description,
        epilog=EPILOG,
        allow_abbrev=False,
        formatter_class=CustomFormatter,
    )
    parser._positionals.title = POSITIONALS_TITLE
    parser._optionals.title = OPTIONALS_TITLE
    parser._actions[0].help = HELP_MESSAGE
    return parser


def initialize_parser(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Initialize the CLI parser.

    Parameters
    ----------
    parser : ArgumentParser
        parser to get user arguments.

    Returns
    -------
    Namespace
        Arguments used and unused.

    """
    return parser.parse_args(sys.argv[1:] or ['--help'])
