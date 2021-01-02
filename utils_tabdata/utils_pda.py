from pandas import ExcelWriter


class UtilsPDA:

    @staticmethod
    def dframes_to_excel_sheets(data_frames, sheet_names, file_name):
        # Creates an excel file with the contents of a data frame per sheet.
        # Precondition: [data_frames].len() = [sheet_names].len().
        try:
            with ExcelWriter(file_name + '.xlsx') as writer:
                ct = 0
                for df in data_frames:
                    df.to_excel(writer, sheet_name=sheet_names[ct], index=False)
                    ct += 1
        except IOError:
            print('File {} could not be created.'.format(file_name))
