from csv import reader
from os import remove
from utils_tabdata import UtilsCSV
import unittest


class TestUtilsCSV(unittest.TestCase):

    def setUp(self):
        a = [{'a': 1, 'b': 8, 'c': 0}, {'a': 2, 'b': 33, 'c': 'zz'}]
        self.auxf = UtilsCSV()
        self.auxf.dicts_to_csv(a, 'test', ['b', 'a', 'c'])
        self.auxf.dicts_to_csv(a, 'test1', ['a', 'b', 'c'])

    def test_unique_rows(self):
        ds = [{'a': '2'}, {'a': '1'}, {'a': '-1'}, {'a': '-1'}]
        ds1 = [{'a': '2', 'b': '0'}, {'a': '1', 'b': '0'}, {'a': '-1', 'b': 'j'}, {'a': '-1', 'b': 'k'}]
        ds2 = [{'a': '1', 'b': '0'}, {'a': '1', 'b': '0'}, {'a': '-1', 'b': 'j'}, {'a': '-1', 'b': 'k'}]
        self.assertListEqual(UtilsCSV().unique_rows(ds, all_columns=True), [{'a': '2'}, {'a': '1'}, {'a': '-1'}])
        self.assertListEqual(
            UtilsCSV().unique_rows(ds1, 'b'), [{'a': '2', 'b': '0'}, {'a': '-1', 'b': 'j'}, {'a': '-1', 'b': 'k'}])
        self.assertListEqual(
            UtilsCSV().unique_rows(ds2, 'a', 'b'), [{'a': '1', 'b': '0'}, {'a': '-1', 'b': 'j'}, {'a': '-1', 'b': 'k'}])

    def test_blank_fields(self):
        a = self.auxf.blank_fields('', '    ', ' ')
        b = self.auxf.blank_fields(' a', '', ' b', '3')
        self.assertTrue(a)
        self.assertFalse(b)

    def test_sort_by_int_in_str(self):
        pattern = [{'a': '1'}, {'a': '2'}, {'a': '-1'}]
        asc_pattern = [{'a': '-1'}, {'a': '1'}, {'a': '2'}]
        desc_pattern = [{'a': '2'}, {'a': '1'}, {'a': '-1'}]
        self.assertListEqual(UtilsCSV().sort_by_int_in_str(pattern, 'a'), asc_pattern)
        self.assertListEqual(UtilsCSV().sort_by_int_in_str(pattern, 'a', reverse=True), desc_pattern)

    def test_dict_list_to_csv_with_ordered_columns(self):
        with open('test.csv') as fh:
            dr = reader(fh)
            self.assertEqual([row for row in dr][0], ['b', 'a', 'c'])

    def test_merge_csvs_with_column_order(self):
        self.auxf.merge_csvs('test2', 'test.csv', 'test1.csv', column_lst=['c', 'a', 'b'])
        with open('test2.csv') as fh:
            dr = reader(fh)
            self.assertEqual([row for row in dr][0], ['c', 'a', 'b'])

    @classmethod
    def tearDownClass(cls):
        remove('test.csv')
        remove('test1.csv')
        remove('test2.csv')
