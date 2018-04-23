# -*- coding: utf-8 -*-
from utils_tabdata.utils_csv import UtilsCSV
import click

# Common strs.
he = 'Encoding to use. Default is UTF-8.'
hd = 'Delimiter to use. Default is ",".'
hf = 'Files to merge. At least two required.'
dd = ','
de = 'utf-8'
argcol = 'column_names'
argtf = 'target_file'
argdf = 'dest_file'
optdel = '--delimiter'
optenc = '--encoding'


@click.group()
def cli():
    pass


@cli.command()
@click.option(optdel, default=dd, help=hd)
@click.option(optenc, default=de, help=he)
@click.argument(argtf, type=click.Path(dir_okay=False))
@click.argument(argdf, type=click.Path(dir_okay=False))
@click.argument(argcol, nargs=-1)
def unique_rows(delimiter, encoding, target_file, dest_file, column_names):
    """Generates a CSV file with the unique rows of target CSV file. By default all columns are compared.
    To check only certain columns input their names as last arguments to the command."""
    rows = UtilsCSV().csv_to_dict_list(target_file, encoding, delimiter)
    if column_names.__len__().__eq__(0):
        res = UtilsCSV().unique_rows(rows, all_columns=True)
    else:
        res = UtilsCSV().unique_rows(rows, *column_names)
    UtilsCSV().dicts_to_csv(res, dest_file, encoding=encoding, delimiter=delimiter)


@cli.command()
@click.option(optdel, default=dd, help=hd)
@click.option(optenc, default=de, help=he)
@click.argument(argcol, nargs=-1)
@click.argument(argdf, type=click.Path(dir_okay=False))
@click.option('--target_file', '-f', multiple=True, type=click.Path(dir_okay=False), help=hf)
def merge_csvs(delimiter, encoding, column_names, dest_file, target_file):
    """Merges CSV files with the same name (header) and number of columns
    (the order may be different in each one though).
    Column order in the output file can be set by passing column names
    (separated by whitespace) in the desired order to the command."""
    UtilsCSV().merge_csvs(dest_file, *target_file, column_lst=column_names, encoding=encoding, delimiter=delimiter)
