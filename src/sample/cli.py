import click
from sample.simple import add_one

@click.command()
@click.argument('number', nargs=1, type=click.INT)
def main(number):
    print(add_one(number))

if __name__ == '__main__':
    main()