def vlookup(search_key, header_row, table, search_column, result_column):
    # Find the index of the search_column and result_column
    try:
        search_index = header_row.index(search_column)
        result_index = header_row.index(result_column)
    except ValueError:
        return None

    # Search for the search_key in the table
    for row in table:
        if row[search_index] == search_key:
            return row[result_index]

    # If search_key is not found, return None
    return None

header_row = ["nama", "npm", "kelas", "nilai"]
table = [["Bambang Sudrajat", 23051, "A", "B+"],
         ["Safira Sudrajat", 23052, "B", "A"],
         ["Huki Kamal", 23102, "B", "A-"],
         ["Andini Azhara", 23100, "C", "B"],
         ["Usep Sakasep", 23013, "D", "A-"]]

print(vlookup(23102, header_row, table, "npm", "nama"))