import click

class Config:
    def __init__(self):
        self.root = False

pass_config = click.make_pass_decorator(Config, ensure=True)
