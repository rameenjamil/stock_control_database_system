"""
Utility functions module for the Stock Control Database application.

This module contains reusable helper functions that support user
interaction, input validation, and formatted table display.

Responsibilities:
- Validate user input
- Handle menu selection logic
- Display formatted tables
- Provide reusable helper functions
"""

import textwrap
from colorama import Fore, Style


def get_choice(prompt, options):
    """
Displays a menu and retrieves a validated user selection.

This function prints a list of options, validates the user's input,
and continues prompting until a valid choice is entered.

Args:
    prompt (str): Menu title or instruction text.
    options (list): List of selectable menu options.

Returns:
    str:
        The validated user choice.
"""

    print(f"\n{prompt}")
    for option in options:
        print(option)

    valid_choices = []
    for option in options:
        number = option.split(".")[0]
        valid_choices.append(number)

    choice = None
    while choice not in valid_choices:
        choice = input("Choose an option: ").strip()
        if choice not in valid_choices:
            error("Invalid choice. Please select a valid option.")
    return choice


def is_valid_name(value):
    """
Validates whether a string contains a properly formatted name.

The validation allows alphabetic characters, spaces, and hyphens,
while rejecting empty or invalid input values.

Args:
    value (str): Input string to validate.

Returns:
    bool:
        True if the name is valid, otherwise False.
"""
    value = value.strip()
    if not value:
        return False
    return value.replace(" ", "").replace("-", "").isalpha()


def print_table(headers, rows, widths):
    """
Prints database records in a formatted table layout.

This utility function aligns columns, truncates overly long values,
and displays structured tabular output for improved readability.

Args:
    headers (list): Column header labels.
    rows (list): Table row data.
    widths (list): Width configuration for each column.

Returns:
    None
"""
    def format_cell(value, width):
        return textwrap.shorten(str(value), width=width, placeholder="...")

    # header printing
    header_line = ""
    for i in range(len(headers)):
        header_line += f"{headers[i]:<{widths[i]}}"
    print(header_line)

    # separator line
    print("-" * sum(widths))

    # print records
    for row in rows:
        row_line = ""
        for i in range(len(row)):
            value = format_cell(row[i], widths[i])
            row_line += f"{value:<{widths[i]}}"
        print(row_line)


def success(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)


def error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)


def warning(msg):
    print(Fore.YELLOW + msg + Style.RESET_ALL)
