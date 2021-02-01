======================
Module utils_tabdata.
======================

Small module with tools to organize and work with tabular data (from CSV files or Pandas Data Frames).

***************
Installation.
***************
git clone https://github.com/Asta1986/utils_tabdata

cd utils_tabdata

pip install .

**To uninstall it:** pip uninstall utils_tabdata

***************
Classes.
***************
**UtilsChart**

    import utils_tabdata.UtilsChart
    
**Public interface**

- plot_timecomplexity(inputsizes, datadict, title='')

Displays a line chart with input size values on the X-axis and execution time values on the Y-axis.

**UtilsCSV**

    import utils_tabdata.UtilsCSV
    
**Public interface**

- csv_to_dict_list(str_csv_file_nm, encoding='utf-8', delimiter=',')

Reads the CSV file received as first argument and returns a list of dictionaries with column names as keys, one for each row in the file.

- dicts_to_csv(row_dict_list, destnm, column_lst=None, encoding='utf-8', delimiter=',')

Writes the list of dictionaries received as first argument to the file path received as second argument.

Parameter column_lst (list of strings of column names) determines column order in the output file.

Precondition: all rows have the same columns.

- unique_rows(row_dict_list, *column_name, all_columns=False)

Returns a list with the unique dicts (rows) of the received list of dictionaries.

Comparisons can be made using all or some of the dict keys (which map the CSV column names).

- sort_by_int_in_str(row_dict_list, column_name, reverse=False)

Returns the list of dicts (rows) received as argument sorted by the column received as second argument which can have numbers or numbers in a string as values (i. e. 3 or "3" but not "a3j").

- blank_fields(*str_fields)

Returns True if the concatenation of received strings has 0 characters or only has space characters.

- merge_csvs(destnm, *csv_path, column_lst=None, encoding='utf-8', delimiter=',')

Combines the specified CSV files into the file path received as first argument. Parameter column_lst determines column order in the output file.

Precondition: all CSVs and all rows have the same columns.

**UtilsPDA**

    import utils_tabdata.UtilsPDA
    
**Public interface**

- dframes_to_excel_sheets(data_frames, sheet_names, file_name)
        
Creates an excel file with the contents of a data frame per sheet.

Precondition: data_frames (list of Pandas Data Frames) and sheet_names (list of strings) have the same number of elements.

**Terminal Commands**

On the command line **'utils_tabdata --help'** can be used to see the available terminal commands.
