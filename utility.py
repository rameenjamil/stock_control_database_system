import textwrap
from colorama import Fore, Style


def get_choice(prompt, options):
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
    value = value.strip()
    if not value:
        return False
    return value.replace(" ", "").replace("-", "").isalpha()


def print_table(headers, rows, widths):
    """
    Utility function to print a formatted table with aligned columns.
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
