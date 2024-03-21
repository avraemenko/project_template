

from input import input_from_console, read_from_file_builtin, read_from_file_pandas
from output import output_to_console, write_to_file_builtin

def main():
    # Input from console
    console_text = input_from_console()
    output_to_console(console_text)
    write_to_file_builtin('data/console_output.txt', console_text)

    # Reading and outputting from a built-in file
    builtin_text = read_from_file_builtin('data/sample.txt')
    output_to_console(builtin_text)
    write_to_file_builtin('data/builtin_output.txt', builtin_text)

    # Reading with pandas (assuming CSV for simplicity)
    # Note: Implement only if your data and use case match, 
    # otherwise adjust or skip accordingly.
    pandas_text = read_from_file_pandas('data/sample.csv')
    output_to_console(pandas_text.to_string())
    write_to_file_builtin('data/pandas_output.txt', pandas_text.to_string())

if __name__ == "__main__":
    main()
