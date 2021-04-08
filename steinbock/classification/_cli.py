import click

from steinbock.classification.ilastik._cli import ilastik
from steinbock.utils import cli


@click.group(
    cls=cli.OrderedClickGroup,
    help="Perform pixel classification to create probability images",
)
def classify():
    pass


classify.add_command(ilastik)
