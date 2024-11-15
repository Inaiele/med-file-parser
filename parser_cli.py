from pathlib import Path
from file_parser import Parser, save_parse_result_to_xlsx
import click

@click.group()
def cli():
    pass

@click.command()
@click.option(
    '-i', '--input-dir', required=True, type=Path,
    help='path to dir with file for parsing.')
@click.option(
    '-o', '--output-dir', required=True, type=Path,
    help='path to dir for saving result.')
def multi_parsing(input_dir : Path, output_dir : Path):
    """
    Do parsing for all files in a directory.

    Args:
        input (_type_): path to directory with files.
        output (_type_): path to directory with output files.
    """
    for item in Path(input_dir).iterdir():
        if item.is_file() and item.name.endswith('.txt'):
            try:
                print('*******************************************************')
                print(f'Parsing {item}')
                parser = Parser(str(Path(item).resolve()))
                res = parser.parse()

                saving_path = Path(output_dir, f'{item.stem}.xlsx')
                print(f'Saving result to {saving_path}')
                save_parse_result_to_xlsx(str(saving_path), res, ['TI', 'AB'])
            except Exception as e:
                print(f'Cannot parse file {item}. {e}')


@click.command()
@click.option(
    '-i', '--input-file', required=True, type=Path,
    help='path to input file.')
@click.option(
    '-o', '--output-file', required=True, type=Path,
    help='path to output file.')
def single_parsing(input_file : Path, output_file : Path):
    """
    Do single file parsing

    Args:
        input_file (_type_): path to input file
        output_file (_type_): path to output file
    """

    print('*******************************************************')
    print(f'Parsing {input_file}')
    parser = Parser(str(input_file.resolve()))
    res = parser.parse()

    print(f'Saving result to {output_file}')
    save_parse_result_to_xlsx(str(output_file), res, ['TI', 'AB'])


cli.add_command(multi_parsing)
cli.add_command(single_parsing)

if __name__ == '__main__':
    cli()