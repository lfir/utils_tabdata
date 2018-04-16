# -*- coding: UTF-8 -*-
from csv import DictWriter, DictReader
from itertools import chain


class UtilsCSV:

    @staticmethod
    def __add_if_not_present(lst, element):
        if element not in lst:
            lst.append(element)

    @staticmethod
    def __add_if_pattern_not_present(lst, element, pattern, patternset):
        pre_size = patternset.__len__()
        patternset.add(pattern)
        pos_size = patternset.__len__()
        if pos_size > pre_size:
            lst.append(element)

    @staticmethod
    # returns a list with the unique dicts (rows) of the received list of dictionaries.
    # comparisons can be made usign all or some of the keys (columns).
    def unique_rows(row_dict_list, *column_name, all_columns=False):
        if len(column_name).__eq__(0) and not all_columns:
            raise TypeError("No column/key names specified.")
        res = []
        if all_columns:
            for row in row_dict_list:
                UtilsCSV.__add_if_not_present(res, row)
        else:
            cmpl = set()
            for row in row_dict_list:
                cmp = tuple(row[col_name] for col_name in column_name)
                UtilsCSV.__add_if_pattern_not_present(res, row, cmp, cmpl)
        return res

    @staticmethod
    def sort_by_int_in_str(row_dict_list, column_name, reverse=False):
        # precondition: values of column_name are ints or ints in strings
        res = []
        for row in row_dict_list:
            res.append((int(row[column_name]), row))
        res = sorted(res, reverse=reverse)
        return [tupl[1] for tupl in res]

    @staticmethod
    def blank_fields(*str_fields):
        # returns True if the concatenation of received strings has 0 characters or only has space characters.
        if (not map(lambda str_field: isinstance(str_field, str), str_fields)) or (len(str_fields).__eq__(0)):
            raise TypeError("No arguments received.")
        res = ''
        for field in str_fields:
            res += field
        return res.__len__().__eq__(0) or res.isspace()

    @staticmethod
    def csv_to_dict_list(str_csv_file_nm, encoding='utf-8', delimiter=','):
        # returns a list of dictionaries with column names as keys, one for each row in the file.
        dict_list = []
        try:
            with open(str_csv_file_nm, encoding=encoding) as fh:
                dr = DictReader(fh, delimiter=delimiter)
                dict_list = [x for x in dr]
        except IOError:
            print('File {} could not be accessed.'.format(str_csv_file_nm))
        return dict_list

    @staticmethod
    def dicts_to_csv(row_dict_list, destnm, column_lst=None, encoding='utf-8', delimiter=','):
        # precondition: all rows have the same columns.
        # column_lst determines column order in the output file.
        destf = destnm + '.csv'
        try:
            with open(destf, 'w', encoding=encoding) as fh:
                if not column_lst:
                    column_lst = row_dict_list[0].keys()
                wr = DictWriter(fh, fieldnames=column_lst, delimiter=delimiter, lineterminator='\n')
                wr.writeheader()
                for row in row_dict_list:
                    wr.writerow(row)
        except IOError:
            print('File {} could not be created.'.format(destf))

    @staticmethod
    def merge_csvs(destnm, *csv_path, column_lst=None, encoding='utf-8', delimiter=','):
        # precondition: all csvs and all rows have the same columns.
        # column_lst determines column order in the output file.
        if len(csv_path) < 2:
            raise TypeError("Less than two file paths received as arguments.")
        rec = []
        for fcsv in csv_path:
            rec.append(UtilsCSV().csv_to_dict_list(fcsv, encoding=encoding, delimiter=delimiter))
        flattened = list(chain.from_iterable(rec))
        UtilsCSV().dicts_to_csv(flattened, destnm, column_lst, encoding=encoding, delimiter=delimiter)
