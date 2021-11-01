==============
utils_tabdata
==============

.. image:: https://github.com/Asta1986/utils_tabdata/actions/workflows/ci.yml/badge.svg

Small module with tools to organize and work with tabular data (from CSV files or Pandas Data Frames).

***************
Installation
***************
git clone https://github.com/Asta1986/utils_tabdata

cd utils_tabdata

pip install .

**To uninstall it:** pip uninstall utils_tabdata

***************
Classes
***************
**UtilsChart**

    from utils_tabdata import UtilsChart
    
**Public interface**

- plot_timecomplexity_

.. _plot_timecomplexity: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_chart.py#L8

**UtilsCSV**

    from utils_tabdata import UtilsCSV
    
**Public interface**

- csv_to_dict_list_

.. _csv_to_dict_list: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_csv.py#L110

- dicts_to_csv_

.. _dicts_to_csv: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_csv.py#L125

- unique_rows_

.. _unique_rows: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_csv.py#L62

- sort_by_int_in_str_

.. _sort_by_int_in_str: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_csv.py#L82

- blank_fields_

.. _blank_fields: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_csv.py#L96

- merge_csvs_

.. _merge_csvs: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_csv.py#L148

**UtilsPDA**

    from utils_tabdata import UtilsPDA
    
**Public interface**

- dframes_to_excel_sheets_

.. _dframes_to_excel_sheets: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_pda.py#L8

- print_numtable_

.. _print_numtable: https://github.com/Asta1986/utils_tabdata/blob/master/utils_tabdata/utils_pda.py#L22

*******************
Terminal Commands
*******************

On the command line **'utils_tabdata --help'** can be used to see the available terminal commands.
