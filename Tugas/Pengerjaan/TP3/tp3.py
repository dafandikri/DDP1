""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY

    Program ini dibuat untuk memenuhi tugas TP 3.

    Program ini akan membaca file csv dan mengembalikan dataframe.
    Mempunyai fungsi-fungsi sebagai berikut:
      1. get_type(a_str)
      2. read_csv(file_name, delimiter = ',')
      3. to_list(dataframe)
      4. get_column_names(dataframe)
      5. get_column_types(dataframe)
      6. head(dataframe, top_n = 10)
      7. info(dataframe)
      8. satisfy_cond(value1, condition, value2)
      9. select_rows(dataframe, col_name, condition, value)
      10. select_cols(dataframe, selected_cols)
      11. count(dataframe, col_name)
      12. mean_col(dataframe, col_name)
      13. show_scatter_plot(x, y, x_label, y_label)
      14. scatter(dataframe, col_name_x, col_name_y)

      (BONUS)
      15. write_csv(file_name_write, dataframe=None, delimiter=",")
      16. get_nama_kolom_user_input()
      17. get_data_user_input(list_nama_kolom)
"""

import matplotlib.pyplot as plt

# Fungsi ini akan mengembalikan tipe data dari a_str
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
    
# Fungsi ini akan membaca file csv dan mengembalikan dataframe
def read_csv(file_name, delimiter = ','):
  # Membaca file csv dan memasukkan ke dalam list 
  f = open(file_name, "r")
  list_csv = f.readlines()
  f.close()

  # Error handling
  if len(list_csv) == 0:
    raise Exception("Tabel tidak boleh kosong.")
  
  data = [line.strip().split(delimiter) for line in list_csv]
  list_nama_kolom = data[0]
  data.pop(0)

  # Membuat list tipe data dari setiap kolom
  list_tipe_data = []
  for i in range(len(list_nama_kolom)):
    tipe_data = "int"
    for j in range(len(data)):
      if get_type(data[j][i]) == "int":
        if tipe_data != "float" and tipe_data != "str":
          tipe_data = "int"
      elif get_type(data[j][i]) == "float":
        if tipe_data != "str":
          tipe_data = "float"
      elif get_type(data[j][i]) == "str":
        tipe_data = "str"
    list_tipe_data.append(tipe_data)

  # Mengubah tipe data pada list data
  for i in range(len(list_nama_kolom)):
    for j in range(len(data)):
      if len(data[j]) != len(list_nama_kolom):
        raise Exception(f"Banyaknya kolom pada baris {j + 1} tidak konsisten.")
      if list_tipe_data[i] == "int":
        data[j][i] = int(data[j][i])
      elif list_tipe_data[i] == "float":
        data[j][i] = float(data[j][i])

  return (data, list_nama_kolom, list_tipe_data)

# Fungsi ini akan mengembalikan list dari dataframe
def to_list(dataframe):
  return dataframe[0]

# Fungsi ini akan mengembalikan list dari nama kolom
def get_column_names(dataframe):
  return dataframe[1]

# Fungsi ini akan mengembalikan list dari tipe kolom
def get_column_types(dataframe):
  return dataframe[2]

# Fungsi ini akan mengembalikan string tabel yang berisi 10 baris pertama dari dataframe
def head(dataframe, top_n = 10):
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
  return out_str
  
# Fungsi ini akan mengembalikan string tabel yang berisi informasi dataframe
def info(dataframe):
  # Inisialisasi memisahkan tuple-tuple menajdi list-list
  kolom = get_column_names(dataframe)
  tipe = get_column_types(dataframe)

  # Membuat string output
  out_str = f"Total Baris = {len(to_list(dataframe))} baris\n\n"
  out_str += "Kolom          Tipe\n"
  out_str += ("-" * 30) + "\n"
  for i in range(len(kolom)):
    out_str += f"{kolom[i]:<15}{tipe[i]:<15}\n"

  return out_str

# Fungsi ini akan mengembalikan True atau False dari comparison antara value1 dan value2
def satisfy_cond(value1, condition, value2):
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

# Fungsi ini akan mengembalikan dataframe yang telah difilter berdasarkan kondisi
def select_rows(dataframe, col_name, condition, value):
  # Inisialisasi memisahkan tuple-tuple menajdi list-list
  data = to_list(dataframe)
  list_nama_kolom = get_column_names(dataframe)
  list_tipe_data = get_column_types(dataframe)

  # Error handling
  if type(col_name) != str:
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  if col_name not in list_nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  if condition not in ["<", "<=", ">", ">=","==", "!="]:
    raise Exception(f"Operator {condition} tidak dikenal.")
  
  # Cari index kolom yang ingin diinput
  index = list_nama_kolom.index(col_name)

  # Jika kolom bertipe string, maka ubah menjadi ascii
  data_ascii = []
  if list_tipe_data[index] == "str":
    data_ascii = [[ord(char) for char in row[index]] for row in data]
    if type(value) == list or type(value) == tuple:
      try:
        value = [ord(char) for char in value]
      except TypeError:
        value = value
    elif type(value) == str:
      value = [ord(char) for char in value]
    elif type(value) != str:
      value = [value]
  
  # Jika kolom bukan string
  elif list_tipe_data[index] != "str":
    if type(value) == list or type(value) == tuple:
      try:
        value = [ord(char) for char in value]
      except TypeError:
        value = value
    elif type(value) == str:
      value = [ord(char) for char in value]
    elif type(value) != str:
      value = [value]

  # Membuat list data baru
  new_data = []
  for i in range(len(data)):
    if list_tipe_data[index] != "str":
      if satisfy_cond(data[i][index], condition, value[0]):
        new_data.append(data[i])
    elif list_tipe_data[index] == "str":
      comparison_value = True
      for j in range(len(data_ascii[i])):
        try:
          if not satisfy_cond(data_ascii[i][j], condition, value[j]):
            comparison_value = False
            break
        except IndexError:
          if not satisfy_cond(data_ascii[i][j], condition, 0):
            comparison_value = False
            break
      if comparison_value == True:
        new_data.append(data[i])

  return (new_data, list_nama_kolom, list_tipe_data)

# Fungsi ini akan mengembalikan dataframe sesuai dengan kolom yang dipilih
def select_cols(dataframe, selected_cols):
  # Inisialisasi memisahkan tuple-tuple menajdi list-list
  data = to_list(dataframe)
  list_nama_kolom = get_column_names(dataframe)
  list_tipe_data = get_column_types(dataframe)

  # Error handling
  if len(selected_cols) == 0:
    raise Exception("Parameter selected_cols tidak boleh kosong.")
  if type(selected_cols) != list and type(selected_cols) != tuple:
    raise Exception("Parameter selected_cols harus bertipe list atau tuple.")
  for selected_col in selected_cols:
    if selected_col not in list_nama_kolom:
      raise Exception(f"Kolom {selected_col} tidak ditemukan.")

  # Membuat list data baru
  selected_data = []
  for row in data:
    selected_row = [row[list_nama_kolom.index(col)] for col in selected_cols]
    selected_type = [list_tipe_data[list_nama_kolom.index(col)] for col in selected_cols]
    selected_data.append(selected_row)

  return selected_data, selected_cols, selected_type

# Fungsi ini akan menghitung jumlah kemunculan nilai unik pada kolom
def count(dataframe, col_name):
  # Inisialisasi memisahkan tuple-tuple menajdi list-list
  data = to_list(dataframe)
  list_nama_kolom = get_column_names(dataframe)

  # Error handling
  if type(col_name) != str:
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  if col_name not in list_nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  if len(data) == 0:
    raise Exception("Tabel kosong.")
  
  # Ambil column yang ingin dihitung
  index = list_nama_kolom.index(col_name)
  col = [row[index] for row in data]

  # Menghitung jumlah kemunculan nilai unik
  frequency_count = {}
  for item in col:
    if item in frequency_count:
      frequency_count[item] += 1
    else:
      frequency_count[item] = 1
  
  return frequency_count

# Fungsi ini akan menghitung rata-rata dari kolom
def mean_col(dataframe, col_name):
  # Inisialisasi memisahkan tuple-tuple menajdi list-list
  data = to_list(dataframe)
  list_nama_kolom = get_column_names(dataframe)
  list_tipe_data = get_column_types(dataframe)

  # Error handling
  if col_name not in list_nama_kolom:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  if type(col_name) != str:
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  index = list_nama_kolom.index(col_name)  

  if list_tipe_data[index] == "str":
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")
  if len(data) == 0:
    raise Exception("Tabel kosong.")
  
  # Ambil column yang ingin dihitung
  col = [row[index] for row in data]

  return sum(col) / len(col)

# Fungsi ini menampilkan scatter plot
def show_scatter_plot(x, y, x_label, y_label):
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()
  
# Fungsi ini memproses dataframe dan call function show_scatter_plot
def scatter(dataframe, col_name_x, col_name_y):
  # Inisialisasi memisahkan tuple-tuple menajdi list-list
  list_nama_kolom = get_column_names(dataframe)
  list_tipe_data = get_column_types(dataframe)

  # Error handling
  if type(col_name_x) != str:
    raise Exception(f"Kolom {col_name_x} harus bertipe string.")
  if type(col_name_y) != str:
    raise Exception(f"Kolom {col_name_y} harus bertipe string.")
  if col_name_x not in list_nama_kolom:
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
  if col_name_y not in list_nama_kolom: 
    raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
  
  # Ambil column yang diinginkan untuk display scatter plot
  index_x = list_nama_kolom.index(col_name_x)
  index_y = list_nama_kolom.index(col_name_y)
  type_x = list_tipe_data[index_x]
  type_y = list_tipe_data[index_y]
  if type_x != "int" and type_x != "float":
    raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
  if type_y != "int" and type_y != "float":
    raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
  
  # Ambil data yang ingin diplot
  x = select_cols(dataframe, [col_name_x])
  y = select_cols(dataframe, [col_name_y])
  x = to_list(x)
  y = to_list(y)

  show_scatter_plot(x, y, col_name_x, col_name_y)

# (BONUS) Fungsi ini akan menulis csv dari input user
def write_csv(file_name_write, dataframe=None, delimiter=","):
  with open(file_name_write, "w") as fw:
    if dataframe is not None:
      list_nama_kolom = get_column_names(dataframe)
      data = [row_read for row_read in to_list(dataframe)] + [row_write for row_write in get_data_user_input(list_nama_kolom)]
    else:
      list_nama_kolom = get_nama_kolom_user_input()
      if not list_nama_kolom:
        raise Exception("Nama kolom harus ada.")
      print()
      data = get_data_user_input(list_nama_kolom)

    fw.write(delimiter.join(list_nama_kolom) + "\n")
    for row in data:
      fw.write(delimiter.join(str(item) for item in row) + "\n")

# (BONUS) Fungsi ini akan mengembalikan list nama kolom dari input user
def get_nama_kolom_user_input():
  list_nama_kolom = []
  while True:
    nama_kolom = input("Masukkan nama kolom (Ketik 'stop' jika ingin berhenti): ")
    if nama_kolom.lower() == "stop":
      return list_nama_kolom
    list_nama_kolom.append(nama_kolom)

# (BONUS) Fungsi ini akan mengembalikan list data dari input user
def get_data_user_input(list_nama_kolom):
  data = []
  while True:
    data_to_write = []
    for nama_kolom in list_nama_kolom:
      input_data = input(f"Masukkan data untuk kolom '{nama_kolom}' (Ketik 'stop' jika ingin berhenti): ")
      if input_data.lower() == "stop":
        return data
      data_to_write.append(input_data)
    data.append(data_to_write)
    print()

# Main program
if __name__ == "__main__":
  df = read_csv("abalone.csv")
  print(head(df))
  print(info(df))
  print(f"Count: {count(df, 'Sex')}")
  print(f"Mean: {mean_col(df, 'Diameter')}")
  df2 = select_rows(select_rows(df, "Length", ">", 0.49), "Sex", "==", "M")
  print(head(df2))
  df3 = select_cols(df, ['Sex', 'Length', 'Diameter', 'Height', 'Rings'])
  print(head(df3))

  # (BONUS) Menulis csv, akan membuat file baru bernama abalone_write.csv menambahkan data dari dataframe
  write_csv("abalone_write.csv", df)