from click.testing import CliRunner
from os import remove
from utils_tabdata import utils_csv, scripts
import unittest


class TestScripts(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()
        self.a = [{'a': 1, 'b': 8, 'c': 0}, {'a': 2, 'b': 33, 'c': 'zz'}]
        self.auxf = utils_csv.UtilsCSV()
        self.auxf.dicts_to_csv(self.a, 'tsur', ['b', 'a', 'c'])
        self.auxf.dicts_to_csv(self.a, 'mergecsv0')
        self.auxf.dicts_to_csv(self.a, 'mergecsv1', ['b', 'a', 'c'])

    def test_unique_rows(self):
        result = self.runner.invoke(scripts.unique_rows, ['tsur.csv', 'restsur0'])
        self.assertEqual(self.auxf.csv_to_dict_list('restsur0.csv'), self.auxf.csv_to_dict_list('tsur.csv'))
        self.assertEqual(result.exit_code, 0)

    def test_unique_rows_some_columns_only(self):
        result = self.runner.invoke(scripts.unique_rows, ['tsur.csv', 'restsur1', 'a'])
        self.assertEqual(self.auxf.csv_to_dict_list('restsur1.csv'), self.auxf.csv_to_dict_list('tsur.csv'))
        self.assertEqual(result.exit_code, 0)

    def test_merge_csvs(self):
        result = self.runner.invoke(scripts.merge_csvs, ['res_merge0', '-f', 'mergecsv0.csv', '-f', 'mergecsv1.csv'])
        self.assertEqual(self.auxf.csv_to_dict_list('res_merge0.csv').__len__(),
                         self.auxf.csv_to_dict_list('mergecsv0.csv').__len__() +
                         self.auxf.csv_to_dict_list('mergecsv1.csv').__len__())
        self.assertEqual(result.exit_code, 0)

    def test_merge_csvs_some_columns_only(self):
        result = self.runner.invoke(scripts.merge_csvs,
                                    ['a', 'c', 'b', 'res_merge1', '-f', 'mergecsv0.csv', '-f', 'mergecsv1.csv'])
        self.assertEqual(self.auxf.csv_to_dict_list('res_merge1.csv').__len__(),
                         self.auxf.csv_to_dict_list('mergecsv0.csv').__len__() +
                         self.auxf.csv_to_dict_list('mergecsv1.csv').__len__())
        self.assertEqual(result.exit_code, 0)

    @classmethod
    def tearDownClass(cls):
        remove('tsur.csv')
        remove('restsur0.csv')
        remove('restsur1.csv')
        remove('res_merge0.csv')
        remove('res_merge1.csv')
        remove('mergecsv0.csv')
        remove('mergecsv1.csv')
