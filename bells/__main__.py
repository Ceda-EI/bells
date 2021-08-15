"Main script for bells"
import logging

import click
from .commands import init


@click.group()
@click.option("-v", "--verbose", is_flag=True,
              help="Verbose mode for printing debug info")
def main(verbose):
    "Bells is a project for storing voice recordings"
    level = logging.FATAL
    if verbose:
        level = logging.DEBUG
    logging.basicConfig(level=level)


main.add_command(init)

if __name__ == '__main__':
    main()  # pylint: disable=E1120
