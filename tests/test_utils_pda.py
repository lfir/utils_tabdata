import unittest
from os import remove
from unittest.mock import patch

import pandas
from utils_tabdata import UtilsPDA


class TestUtilsPDA(unittest.TestCase):
    def setUp(self):
        self.auxf = UtilsPDA()
        d1 = {"fst": [1.0, 2.0, 3.0, 4.0], "snd": [4.0, 3.0, 2.0, 1.0]}
        d2 = {"trd": [5, 6, 7, 8], "fth": [8, 7, 6, 5]}
        self.df1 = pandas.DataFrame(d1)
        self.df2 = pandas.DataFrame(d2)
        self.dfs = [self.df1, self.df2]

    def test_data_frames_to_sheets_of_excel_spreadsheet(self):
        self.auxf.dframes_to_excel_sheets(self.dfs, ["t1", "t2"], "testdf")
        with pandas.ExcelFile("testdf.xlsx") as xls:
            df1 = pandas.read_excel(xls, "t1")
            df2 = pandas.read_excel(xls, "t2")

            self.assertTrue(
                df1.keys().__contains__("fst")
                and df1.keys().__contains__("snd")
                and df1.keys().__len__().__eq__(2)
            )
            self.assertTrue(
                df2.keys().__contains__("trd")
                and df2.keys().__contains__("fth")
                and df1.keys().__len__().__eq__(2)
            )
            self.assertListEqual(
                [value for value in df1.get("fst")], [1.0, 2.0, 3.0, 4.0]
            )
            self.assertListEqual(
                [value for value in df1.get("snd")], [4.0, 3.0, 2.0, 1.0]
            )
            self.assertListEqual([value for value in df2.get("trd")], [5, 6, 7, 8])
            self.assertListEqual([value for value in df2.get("fth")], [8, 7, 6, 5])

    @patch("builtins.print")
    def test_when_print_numtable_called_invokes_pandas_dataframe(self, mock_print):
        table = [[1, 2], [3, 4]]
        UtilsPDA.print_numtable(table)

        mock_print.assert_called_once()
        assert isinstance(mock_print.call_args_list[0][0][0], pandas.DataFrame)

    @classmethod
    def tearDownClass(cls):
        remove("testdf.xlsx")
