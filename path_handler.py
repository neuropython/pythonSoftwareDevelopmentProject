# -*- coding: utf-8 -*
import os
import pandas as pd


class PathHandler:
    def __init__(self, path_to_a_directory, names_of_variables, delimiter=';'):
        self.path_to_a_directory = path_to_a_directory
        self.names_of_the_files_to_search_from = names_of_variables
        self.delimiter = delimiter
        self.signals = self.get_signals_from_files()

    def get_all_csv_files(self):
        all_files = os.listdir(self.path_to_a_directory)
        csv_files = [file for file in all_files if file.endswith('.csv')]
        return csv_files

    def get_signals_from_files(self):
        csv_files = self.get_all_csv_files()
        signals = [pd.read_csv(fr"{self.path_to_a_directory}/{i}", delimiter=self.delimiter) for i in csv_files]
        signal_from_names = [i[name] for i in signals for name in self.names_of_the_files_to_search_from if
                             name in i.columns]
        return signal_from_names


if __name__ == "__main__":
    path = r"example_data"
    names = ['abp_finger_mm_hg_[abp_finger_mm_Hg_]']
    ph = PathHandler(path, names)
    print(ph.signals)