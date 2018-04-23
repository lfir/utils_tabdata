# -*- coding: UTF-8 -*-
from collections import OrderedDict
from csv import DictWriter, DictReader
from itertools import chain, filterfalse


class UtilsCSV:

    @staticmethod
    def __dict_to_tuple(d):
        # Freezes dict (can be hashed).
        # Precondition: values of the dictionary are themselves immutable (e.g. strings).
        if isinstance(d, dict):
            return tuple((k, d[k]) for k in d)
        else:
            raise TypeError("Expected argument of type dict. Received {}.".format(type(d)))

    @staticmethod
    def __tuple_to_dict(t):
        if isinstance(t, tuple):
            return OrderedDict(t)
        else:
            raise TypeError("Expected argument of type tuple. Received {}.".format(type(t)))

    @staticmethod
    def __dict_list_to_tuple_of_tuples(dl):
        # Returns ((k0, v0), (k1, v1), .. (kn, vn))
        if isinstance(dl, list):
            return tuple(UtilsCSV.__dict_to_tuple(d) for d in dl)
        else:
            raise TypeError("Expected argument of type list. Received {}.".format(type(dl)))

    @staticmethod
    def __unique_everseen(iterable, key=None):
        # List unique elements, preserving order. Remember all elements ever seen.
        # unique_everseen('AAAABBBCCDAABBB') --> A B C D
        # unique_everseen('ABBCcAD', str.lower) --> A B C D
        # https://docs.python.org/3.6/library/itertools.html#itertools-recipes
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in filterfalse(seen.__contains__, iterable):
                seen_add(element)
                yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element

    @staticmethod
    def __add_if_pattern_not_present(lst, element, pattern, patternset):
        pre_size = patternset.__len__()
        patternset.add(pattern)
        pos_size = patternset.__len__()
        if pos_size > pre_size:
            lst.append(element)

    @staticmethod
    def unique_rows(row_dict_list, *column_name, all_columns=False):
        # Returns a list with the unique dicts (rows) of the received list of dictionaries.
        # Comparisons can be made using all or some of the keys (columns).
        if len(column_name).__eq__(0) and not all_columns:
            raise TypeError("No column/key names specified.")
        res = []
        if all_columns:
            gen = UtilsCSV().__unique_everseen(UtilsCSV().__dict_list_to_tuple_of_tuples(row_dict_list))
            res = [UtilsCSV().__tuple_to_dict(x) for x in gen]
        else:
            cmpl = set()
            for row in row_dict_list:
                cmp = tuple(row[col_name] for col_name in column_name)
                UtilsCSV().__add_if_pattern_not_present(res, row, cmp, cmpl)
        return res

    @staticmethod
    def sort_by_int_in_str(row_dict_list, column_name, reverse=False):
        # Precondition: values of column_name are ints or ints in strings
        res = []
        for row in row_dict_list:
            res.append((int(row[column_name]), row))
        res = sorted(res, reverse=reverse)
        return [tupl[1] for tupl in res]

    @staticmethod
    def blank_fields(*str_fields):
        # Returns True if the concatenation of received strings has 0 characters or only has space characters.
        if (not map(lambda str_field: isinstance(str_field, str), str_fields)) or (len(str_fields).__eq__(0)):
            raise TypeError("No valid (type str) arguments received.")
        res = ''
        for field in str_fields:
            res += field
        return res.__len__().__eq__(0) or res.isspace()

    @staticmethod
    def csv_to_dict_list(str_csv_file_nm, encoding='utf-8', delimiter=','):
        # Returns a list of dictionaries with column names as keys, one for each row in the file.
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
        # Precondition: all rows have the same columns.
        # column_lst determines column order in the output file.
        destf = destnm + '.csv'
        try:
            with open(destf, 'w', encoding=encoding) as fh:
                if not column_lst:
                    column_lst = row_dict_list[0].keys()
                elif column_lst.__len__() != row_dict_list[0].keys().__len__():
                    raise TypeError('Number of columns mismatch between received args and list dicts header.')
                wr = DictWriter(fh, fieldnames=column_lst, delimiter=delimiter, lineterminator='\n')
                wr.writeheader()
                for row in row_dict_list:
                    wr.writerow(row)
        except IOError:
            print('File {} could not be created.'.format(destf))

    @staticmethod
    def merge_csvs(destnm, *csv_path, column_lst=None, encoding='utf-8', delimiter=','):
        # Precondition: all csvs and all rows have the same columns.
        # column_lst determines column order in the output file.
        if len(csv_path) < 2:
            raise TypeError("Less than two file paths received as arguments.")
        rec = []
        for fcsv in csv_path:
            rec.append(UtilsCSV().csv_to_dict_list(fcsv, encoding=encoding, delimiter=delimiter))
        flattened = list(chain.from_iterable(rec))
        UtilsCSV().dicts_to_csv(flattened, destnm, column_lst, encoding=encoding, delimiter=delimiter)
