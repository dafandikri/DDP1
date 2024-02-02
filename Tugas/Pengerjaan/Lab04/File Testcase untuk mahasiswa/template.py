import sys

# Helper function: Print table headers
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# TODO: Implement the function to print the entire table content.
def print_table(filename):
    with open(filename, "r") as f:
        print_headers()
        # Your code here...


# TODO: Implement the function to search for a specific substring, Case insensitive.
# Your code here...


# TODO: Implement the function to get descriptive statistics for a specific column.
# Your code here...


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    # TODO: Call the necessary functions here.