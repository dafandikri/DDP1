import sys

# Fungsi untuk menge-print header table


def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")


# Fungsi untuk menge-print table yang berada di text file
def print_table(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            print_headers()
            number = 1
            for line in lines:
                value = line.strip().split("\t")
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(number, value[0], value[1],
                                                                                value[2], value[3]))
                number += 1

    except FileNotFoundError:
        print("Maaf, file input tidak ada")


# Mencocokkan kata kunci dengan phone yang ada di file txt
def search_phone(filename, keyword):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            line_number = 1
            match_found = False
            for line in lines:
                value = line.strip().split("\t")
                if keyword.lower() in value[0].lower():
                    if not match_found:
                        print_headers()
                        match_found = True
                    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(line_number, value[0], value[1],
                                                                                    value[2], value[3]))
                    line_number += 1
            if not match_found:
                print("Tidak ada smartphone yang cocok dengan kata kunci:", keyword)

    except FileNotFoundError:
        print("Maaf, file input tidak ada")


# Memberi statistik kolom sesuai kemauan user
def desc_stat(filename, column):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            line_number = 1
            maxdata = 0
            mindata = 9999999
            total = 0
            count = 0
            for line in lines:
                value = line.strip().split("\t")
                if len(value) <= column:
                    print("Kolom yang dipilih tidak valid")
                    return
                value = float(value[column])
                if value > maxdata:
                    maxdata = value
                if value < mindata:
                    mindata = value
                total += value
                count += 1
                line_number += 1

            if count > 0:
                average = total / count
                print("Min data: {:.2f}".format(mindata))
                print("Max data: {:.2f}".format(maxdata))
                print("Rata-rata: {:.2f}".format(average))

    except FileNotFoundError:
        print("Maaf, file input tidak ada")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    # Memanggil fungsi
    print_table(file_path)
    print()
    search_phone(file_path, key)
    print()
    desc_stat(file_path, column_num)


