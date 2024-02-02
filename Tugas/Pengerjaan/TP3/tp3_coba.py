# Kita perlu import matplotlib untuk sebuah visualisasi
# Scatter Plot. 
#
# Apa itu Scatter plot?
#   https://chartio.com/learn/charts/what-is-a-scatter-plot/
#
# Jika Anda tidak bisa import matplotlib, ada kemungkinan 
# Anda belum install library matplotlib di local komputer 
# Anda. Silakan ikuti petunjuk pada
# https://matplotlib.org/stable/users/installing/index.html

import matplotlib.pyplot as plt

def get_type(a_str):
  """
    -- DIBUKA KE PESERTA --
    
    Fungsi ini akan mengembalikan tipe dari literal
    string a_str.
    
    get_type("0.5") -> "float"
    get_type("5.") -> "float"
    get_type("5") -> "int"
    get_type("5.a") -> "str"
    
    parameter:
    a_str (string): string literal dari sebuah nilai
    
    return (string): "int", "float", atau "str"
  """
  try:
    int(a_str)
    return "int"
  except:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter=','):
  with open(file_name, 'r') as f:
    lines = f.read().splitlines()

  if not lines:
    raise Exception("Tabel tidak boleh kosong.")

  column_names = lines[0].split(delimiter)
  data = []
  for i, line in enumerate(lines[1:], start=2):
    row = line.split(delimiter)
    if len(row) != len(column_names):
      raise Exception(f"Banyaknya kolom pada baris {i} tidak konsisten.")
    data.append(row)

  column_types = ['str'] * len(column_names)
  for row in data:
    for i, cell in enumerate(row):
      try:
        int(cell)
        column_types[i] = 'int'
      except ValueError:
        try:
          float(cell)
          column_types[i] = 'float'
        except ValueError:
          column_types[i] = 'str'

  return data, column_names, column_types

def to_list(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
    
    mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of lists of items
  """
  return dataframe[0]

def get_column_names(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of column names
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of type names
  """
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
  
    -- DIBUKA KE PESERTA --
  
    top_n baris pertama pada tabel!
  
    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:
    
     kolom_1|     kolom_2|     kolom_3|     ...
    ------------------------------------------- 
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...
    
    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja
    
    return (string): representasi string dari penampilan tabel.
    
    Jangan pakai print()! tetapi return string!
  """
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
  return out_str
  
def info(dataframe):
  data, column_names, column_types = dataframe

  total_rows = len(data)
  output = f"Total Baris = {total_rows} baris\n\n"

  output += f"{'Kolom':<15}Tipe\n"
  output += "-" * 30 + "\n"

  for name, type_ in zip(column_names, column_types):
    output += f"{name:<15}{type_}\n"

  return output

def satisfy_cond(value1, condition, value2):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
  if condition == "<":
    return value1 < value2
  elif condition == "<=":
    return value1 <= value2
  elif condition == ">":
    return value1 > value2
  elif condition == ">=":
    return value1 >= value2
  elif condition == "!=":
    return value1 != value2
  elif condition == "==":
    return value1 == value2
  else:
    raise Exception(f"Operator {condition} tidak dikenal.")

def select_rows(dataframe, col_name, condition, value):
  data, column_names, column_types = dataframe
  print(column_names)

  if col_name not in column_names:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")

  if condition not in ["<", "<=", "==", ">", ">=", "!="]:
    raise Exception(f"Operator {condition} tidak dikenal.")

  col_index = column_names.index(col_name)
  new_data = []

  for row in data:
    if satisfy_cond(row[col_index], condition, value):
      new_data.append(row)

  return new_data, column_names, column_types
  
def select_cols(dataframe, selected_cols):
  data, column_names, column_types = dataframe

  if not selected_cols:
    raise Exception("Parameter selected_cols tidak boleh kosong.")

  for selected_col in selected_cols:
    if selected_col not in column_names:
      raise Exception(f"Kolom {selected_col} tidak ditemukan.")

  new_data = []
  new_column_names = []
  new_column_types = []

  for i, col_name in enumerate(column_names):
    if col_name in selected_cols:
      new_column_names.append(col_name)
      new_column_types.append(column_types[i])
      new_data.append([row[i] for row in data])

  return new_data, new_column_names, new_column_types

def count(dataframe, col_name):
  data, column_names, column_types = dataframe

  if len(data) == 0:
    raise Exception("Tabel kosong.")

  if col_name not in column_names:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")

  col_index = column_names.index(col_name)
  if column_types[col_index] != 'str':
    raise Exception(f"Kolom {col_name} harus bertipe string.")

  freq_count = {}
  for row in data:
    value = row[col_index]
    if value in freq_count:
      freq_count[value] += 1
    else:
      freq_count[value] = 1

  return freq_count

def mean_col(dataframe, col_name):
  data, column_names, column_types = dataframe

  if len(data) == 0:
    raise Exception("Tabel kosong.")

  if col_name not in column_names:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")

  col_index = column_names.index(col_name)
  if column_types[col_index] not in ['int', 'float']:
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

  total = 0
  count = 0
  for row in data:
    total += row[col_index]
    count += 1

  return total / count
  
def show_scatter_plot(x, y, x_label, y_label):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
  """
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()
  
def scatter(dataframe, col_name_x, col_name_y):
  data, column_names, column_types = dataframe

  if len(data) == 0:
    raise Exception("Tabel kosong.")

  if col_name_x not in column_names:
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")

  if col_name_y not in column_names:
    raise Exception(f"Kolom {col_name_y} tidak ditemukan.")

  col_index_x = column_names.index(col_name_x)
  if column_types[col_index_x] not in ['int', 'float']:
    raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")

  col_index_y = column_names.index(col_name_y)
  if column_types[col_index_y] not in ['int', 'float']:
    raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")

  x = [row[col_index_x] for row in data]
  y = [row[col_index_y] for row in data]

  show_scatter_plot(x, y, col_name_x, col_name_y)

if __name__ == "__main__":
  # Read the data from a CSV file
  dataframe = read_csv("abalone.csv")

  # Print the information about the dataframe
  print(info(dataframe))

  # Select rows where a certain condition is met
  new_dataframe = select_rows(dataframe, "Sex", "==", "M")
  print(head(new_dataframe))

  # Select certain columns
  new_dataframe = select_cols(dataframe, ["Diameter", "Height"])
  print(head(new_dataframe))

  # Count the frequency of a certain column
  print(count(dataframe, "Sex"))

  # Calculate the mean of a certain column
  print(mean_col(dataframe, "Rings"))

  # Show a scatter plot of two columns
  scatter(dataframe, "Length", "Diameter")