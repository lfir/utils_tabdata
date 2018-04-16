import unittest
from os import remove

import pandas

from utils_tabdata import UtilsPDA


class TestUtilsPDA(unittest.TestCase):

    def setUp(self):
        self.auxf = UtilsPDA()
        d1 = {'fst': [1., 2., 3., 4.],
              'snd': [4., 3., 2., 1.]}
        d2 = {'trd': [5, 6, 7, 8],
              'fth': [8, 7, 6, 5]}
        self.df1 = pandas.DataFrame(d1)
        self.df2 = pandas.DataFrame(d2)
        self.dfs = [self.df1, self.df2]

    def test_data_frames_to_sheets_of_excel_spreadsheet(self):
        self.auxf.dframes_to_excel_sheets(self.dfs, ['t1', 't2'], 'testdf')
        with pandas.ExcelFile('testdf.xlsx') as xls:
            df1 = pandas.read_excel(xls, 't1')
            df2 = pandas.read_excel(xls, 't2')
            self.assertTrue(df1.keys().__contains__('fst') and df1.keys().__contains__('snd')
                            and df1.keys().__len__().__eq__(2))
            self.assertTrue(df2.keys().__contains__('trd') and df2.keys().__contains__('fth')
                            and df1.keys().__len__().__eq__(2))
            self.assertListEqual([value for value in df1.get('fst')], [1., 2., 3., 4.])
            self.assertListEqual([value for value in df1.get('snd')], [4., 3., 2., 1.])
            self.assertListEqual([value for value in df2.get('trd')], [5, 6, 7, 8])
            self.assertListEqual([value for value in df2.get('fth')], [8, 7, 6, 5])

    def tearDown(self):
        remove('testdf.xlsx')
