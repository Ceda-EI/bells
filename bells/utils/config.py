"Configuration class and decorator"
import click

from .get_root import get_root

class Config:
    "Config class"
    def __init__(self):
        self.root = get_root()

pass_config = click.make_pass_decorator(Config, ensure=True)
