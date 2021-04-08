import click

from steinbock.preprocessing.hifi._cli import hifi
from steinbock.preprocessing.imc._cli import imc
from steinbock.utils import cli


@click.group(
    cls=cli.OrderedClickGroup,
    help="Extract and preprocess images from raw data",
)
def preprocess():
    pass


preprocess.add_command(hifi)
preprocess.add_command(imc)
