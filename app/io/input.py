import pandas as pd


def input_from_console():
    """
    Function to input text from the console.
    """
    return input("Please enter some text: ")


def read_from_file_builtin(filename):
    """
    Function to read from a file using Python's built-in capabilities.

    Args:
        filename (str): Path to the file to be read.
    """
    with open(filename, 'r') as file:
        return file.read()


def read_from_file_pandas(filename):
    """
    Function to read from a file using the pandas library.

    Args:
        filename (str): Path to the file to be read.
    """
    return pd.read_csv(filename)
