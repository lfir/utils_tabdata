import unittest
from unittest.mock import Mock

from utils_tabdata.utils_chart import UtilsChart, plt


class TestScripts(unittest.TestCase):

    def test_plot_called_with_correct_params(self):
        plt.plot = Mock()
        plt.show = Mock()
        plt.title = Mock()
        testtitle = 'Chart1.0'
        inputsizes = [1, 2, 3]
        datadict = {'t0': [50, 500, 5000], 't1': [150, 600, 4000]}

        UtilsChart.plot_timecomplexity(inputsizes, datadict, testtitle)

        plt.plot.call_count == 2
        plt.title.assert_called_once_with(testtitle)
        plt.show.assert_called_once()
