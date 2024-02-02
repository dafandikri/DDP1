
import matplotlib.pyplot as plt

def get_type(a_str):
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"

def read_csv_robust(file_name, delimiter=','):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    data = [line.strip().split(delimiter) for line in lines]
    column_names = data[0]
    data = data[1:]

    for j in range(len(data)):
        for i in range(len(column_names)):
            cell = data[j][i].strip() if isinstance(data[j][i], str) else data[j][i]
            if cell.replace('.', '', 1).isdigit():
                data[j][i] = float(cell) if '.' in cell else int(cell)

    column_types = []
    for i in range(len(column_names)):
        if all(isinstance(row[i], int) for row in data):
            column_types.append("int")
        elif all(isinstance(row[i], (int, float)) for row in data):
            column_types.append("float")
        else:
            column_types.append("str")

    return data, column_names, column_types

def get_column_names(dataframe):
    return dataframe[1]

def get_column_types(dataframe):
    return dataframe[2]

def select_cols(dataframe, cols):
    col_indices = [dataframe[1].index(col) for col in cols]
    selected_data = [[row[i] for i in col_indices] for row in dataframe[0]]
    return selected_data, cols, [dataframe[2][i] for i in col_indices]

def to_list(dataframe):
    return dataframe[0]

def show_scatter_plot(x, y, col_name_x, col_name_y):
    plt.scatter(x, y)
    plt.xlabel(col_name_x)
    plt.ylabel(col_name_y)
    plt.title(f"Scatter Plot of {col_name_x} vs {col_name_y}")
    plt.show()

if __name__ == "__main__":
    df = read_csv_robust("abalone.csv")
    print(get_column_names(df))
    print(get_column_types(df))
    selected_data = select_cols(df, ["Sex", "Length", "Diameter", "Height", "Rings"])
    x, y = to_list(selected_data[0]), to_list(selected_data[1])
    show_scatter_plot(x, y, "Length", "Diameter")