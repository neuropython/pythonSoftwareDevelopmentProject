# -*- coding: utf-8 -*
import os
import pandas as pd


class PathHandler:
    """
    This class is responsible for handling the path to the directory with the data.

    Attributes
    ----------
    path_to_a_directory : rawstr
        The path to the directory with the data.
    names_of_the_files_to_search_from : list
        The names of the files to search from.
    delimiter : str
        The delimiter of the csv files.

    Methods
    -------
    get_all_csv_files()
        Returns all csv files from the directory.
    get_signals_from_files()
        Returns the signals from the files.
    """

    def __init__(self, path_to_a_directory, names_of_variables, delimiter=';'):
        """
        Initialize the class.
        Args:
            path_to_a_directory (rawstring): path to the directory with the data.
            names_of_variables (string): names of the variables to search from.
            delimiter (str, optional): delimter in a csv file. Defaults to ';'.

        Returns:
            None


        """

        self.path_to_a_directory = path_to_a_directory
        self.names_of_the_files_to_search_from = names_of_variables
        self.delimiter = delimiter
        self.all_alaized_files_names = []
        self.all_alaized_names = []
        self.signals = self.get_signals_from_files()

    def get_all_csv_files(self):
        """get all csv files from the directory.

        Returns:
            list: list of csv files names. 
        """
        # get all files from the directory
        all_files = os.listdir(self.path_to_a_directory)

        # get only csv files
        csv_files = [file for file in all_files if file.endswith('.csv')]

        return csv_files
    
    @staticmethod
    def data_cleaner(list):
        """
        clean the data.

        Args:
            list (int): list of data.

        Returns:
            list: list of cleaned data.
        """
        # Remove nan values from signal
        list = list.dropna()

        # Remove 0 values from signal and change ',' to '.' also change str to float
        cleaned = [float(i.replace(',', '.')) for i in list if i != 0]
        return cleaned
    
    def get_signals_from_files(self):
        """
        get the signals from the files.

        Returns:
           DataFrame: pandas dataframe of all signals.
        """

        # Get all csv files from the directory
        csv_files = self.get_all_csv_files()

        # Get signals from files
        signals = {i:pd.read_csv(fr"{self.path_to_a_directory}/{i}", delimiter=self.delimiter)
                   for i in csv_files}

        # Get signals from names
        signal_from_names = []
        for i,k in zip(signals.values(), signals.keys()):
            for name in self.names_of_the_files_to_search_from:
                if name in i.columns:
                    signal_from_names.append(i[name])
                    self.all_alaized_files_names.append(k)
                    self.all_alaized_names.append(name)

        # Clean the data
        signal_from_names_cleared = [PathHandler.data_cleaner(i) for i in signal_from_names]

        # Return signals
        return signal_from_names_cleared


if __name__ == "__main__":
    path = r"C:\Users\damia\OneDrive\Pulpit\data"
    names = ['abp_finger_mm_hg_[abp_finger_mm_Hg_]', 'ekg__[ekg__]']
    ph = PathHandler(path, names)
    print(ph.signals)
    print(ph.all_alaized_files_names)
    print(ph.all_alaized_names)