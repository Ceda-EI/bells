"Main script for bells"
import logging

import click
from .commands import init, rec


@click.group()
@click.option("-v", "--verbose", is_flag=True,
              help="Verbose mode for printing debug info")
def main(verbose):
    "Bells is a project for storing voice recordings"
    level = logging.WARN
    if verbose:
        level = logging.DEBUG
    logging.basicConfig(level=level)


main.add_command(init)
main.add_command(rec)

if __name__ == '__main__':
    main()  # pylint: disable=E1120
