def output_to_console(text):
    """
    Function to output text to the console.

    Args:
        text (str): Text to be printed.
    """
    print(text)


def write_to_file_builtin(filename, text):
    """
    Function to write to a file using Python's built-in capabilities.

    Args:
        filename (str): Path to the file where the text will be written.
        text (str): Text to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(text)
