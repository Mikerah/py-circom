import click

@click.command()
@click.option('-o', '--output', help="Specify output circuit file")
@click.argument('INPUT_SOURCE_INPUT_FILE', help="Specify input circom file")
def circom():
    pass
