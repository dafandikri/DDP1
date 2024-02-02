""" Nama: Erdafa Andikri
    NPM: 2306244993
    Kode Asdos: ROY

    Program ini dibuat untuk memenuhi tugas TP 4.

    Program ini dapat menghasilkan barcode EAN-13 dengan input kode 12 digit desimal.
    User dapat memasukkan nama file dan kode yang akan dijadikan barcode.
    Program akan mengkalkulasi check digit dari input kode.
    Menghasilkan barcode dengan struktur yang sesuai dengan input kode.
    Menampilkan negara asal produk (BONUS)
    Menyimpan barcode ke dalam file PS (PostScript) dengan nama file yang diinput.

    Jika user memasukkan nama file yang tidak sesuai, maka akan muncul error message.
    Jika user memasukkan kode yang tidak sesuai, maka akan muncul error message.
"""

# Import tkinter messagebox and Canvas
import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas

# BONUS - Import country codes
from bonus_tp4_country_codes import country_codes

class Window:
    # Set window size and position
    def __init__(self):
        self.window = tk.Tk()
        window_width = 500
        window_height = 500
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.window.resizable(False, False)

# Class Barcode inherit Window
class Barcode(Window):
    def __init__(self):
        super().__init__()

        # Set window title
        self.window.title("EAN-13 [By Erdafa Andikri]")

        # Set structure of each digit
        self.structure = {
            '0' : 'LLLLLL',
            '1' : 'LLGLGG',
            '2' : 'LLGGLG',
            '3' : 'LLGGGL',
            '4' : 'LGLLGG',
            '5' : 'LGGLLG',
            '6' : 'LGGGLL',
            '7' : 'LGLGLG',
            '8' : 'LGLGGL',
            '9' : 'LGGLGL'
        }

        # Set encoding digits (L)
        self.L_encoding_digits = {
            '0': '0001101',
            '1': '0011001',
            '2': '0010011',
            '3': '0111101',
            '4': '0100011',
            '5': '0110001',
            '6': '0101111',
            '7': '0111011',
            '8': '0110111',
            '9': '0001011',
        }
        
        # Set encoding digits (R)
        complement_mapping = str.maketrans('01', '10')
        self.R_encoding_digits = {key: value.translate(complement_mapping) for key, value in self.L_encoding_digits.items()}

        # Set encoding digits (G)
        self.G_encoding_digits = {key: value[::-1] for key, value in self.R_encoding_digits.items()}

        # Set country codes
        try:
            self.country_codes = country_codes
        except:
            self.country_codes = None

        # User input and Canvas
        self.input()
        self.canvas = Canvas(self.window, width=500, height=400, bg="white")
        self.canvas.pack()
        self.window.mainloop()

    # User input Function
    def input(self):
        # Input filename
        self.label = tk.Label(self.window, text="Save Barcode to PS file [eg: EAN13.eps]:")
        self.label.pack()
        self.filename_entry = tk.Entry(self.window)
        self.filename_entry.pack()

        # Input code
        self.label = tk.Label(self.window, text="Enter code [First 12 decimal digits]:")
        self.label.pack()
        self.code_entry = tk.Entry(self.window)
        self.code_entry.pack()

        # Button and bind Enter key
        self.button = tk.Button(self.window, text="Generate Barcode", command=self.generate_barcode).pack()
        self.window.bind('<Return>', self.generate_barcode)

    # Calculate barcode Function
    def calculate_barcode(self, code):
        # First digit and its structure
        first_digit = code[0]
        first_digit_structure = self.structure[first_digit]

        # Checksum
        code += self.checksum(code)
        barcode_digits = code[1:]

        # Get country (BONUS)
        country = None
        if self.country_codes is not None:
            key = list(self.country_codes.keys())
            if code[:3] in key:
                country = self.country_codes[code[:3]]
            elif code[:2] in key:
                country = self.country_codes[code[:2]]

        return first_digit, first_digit_structure, barcode_digits, country

    # Generate barcode Function
    def generate_barcode(self, event=None):
        # Get filename and code entry
        self.filename = self.filename_entry.get()
        self.code = self.code_entry.get()

        # Check if filename and code entry is valid
        if not self.filename.endswith(".eps"):
            messagebox.showerror("Wrong input!", "Please enter correct file name")
        elif len(self.code) != 12 or not self.code.isdigit():
            messagebox.showerror("Wrong input!", "Please enter correct input code")
        else:
            # Calculate barcode
            self.first_digit, self.first_digit_structure, self.barcode_digits, self.country = self.calculate_barcode(self.code)

            # Draw barcode
            self.canvas.delete("all")
            self.draw_barcode(self.first_digit, self.first_digit_structure, self.barcode_digits, self.country)
            self.canvas.update()

            # Save barcode to PS file
            self.canvas.postscript(file=self.filename, colormode='color')
            messagebox.showinfo("Success!", f"Barcode has been saved to {self.filename}")
    
    # Encode digit Function
    def encode_digit_L(self, digit):
        return self.L_encoding_digits[digit]
    def encode_digit_G(self, digit):
        return self.G_encoding_digits[digit]
    def encode_digit_R(self, digit):
        return self.R_encoding_digits[digit]
            
    # Draw barcode Function
    def draw_barcode(self, first_digit, first_digit_structure, barcode_digits, country):
        line_width = 4
        barcode_width = (len(barcode_digits) + 2) * 7 * line_width  # Each digit and marker is 7 lines wide
        x = (self.canvas.winfo_width() - barcode_width) / 2  # Start drawing from the center
        y = 20  # Starting y coordinate
        height = 150  # Height of barcodes
        marker_height = 170  # Height of the markers

        # Title
        self.create_text = self.canvas.create_text(self.canvas.winfo_width() / 2, y, text="EAN-13 Barcode:", font=("Arial", line_width*7), fill="black")
        y += line_width * 7
        digit_y = y + marker_height
        check_digit_y = digit_y + line_width * 7
        country_y = check_digit_y + line_width * 7 

        # First digit text
        self.canvas.create_text(x, digit_y, text=first_digit, font=("Arial", line_width*7), fill="black")  # Draw the digit
        x += line_width * 3

        # Draw start marker
        for bit in '101':
            if bit == '1':
                self.canvas.create_line(x, y, x, y + marker_height, fill="blue", width=line_width)
            x += line_width

        # Draw barcode 1-6
        for i, digit in enumerate(barcode_digits[:6]):
            encoding = self.encode_digit_L(digit) if first_digit_structure[i] == 'L' else self.encode_digit_G(digit)
            for i, bit in enumerate(encoding):
                if bit == '1':
                    self.canvas.create_line(x, y, x, y + height, fill="black", width=line_width)
                x += line_width
                # Draw the digit
                if i == 3:
                    self.canvas.create_text(x, digit_y, text=digit, font=("Arial", line_width*7), fill="black")  # Draw the digit

        # Draw center marker
        for bit in '01010':
            if bit == '1':
                self.canvas.create_line(x, y, x, y + marker_height, fill="blue", width=line_width)
            x += line_width

        # Draw barcode 7-12
        for digit in barcode_digits[6:]:
            encoding = self.encode_digit_R(digit)
            for i, bit in enumerate(encoding):
                # Draw the digit
                if i == 3:
                    self.canvas.create_text(x, digit_y, text=digit, font=("Arial", line_width*7), fill="black")
                if bit == '1':
                    self.canvas.create_line(x, y, x, y + height, fill="black", width=line_width)
                x += line_width

        # Draw end marker
        for bit in '101':
            if bit == '1':
                self.canvas.create_line(x, y, x, y + marker_height, fill="blue", width=line_width)
            x += line_width

        # Draw check digit
        self.canvas.create_text(self.canvas.winfo_width() / 2, check_digit_y, text=f"Check Digit: {self.code[-1]}", font=("Arial", line_width*7), fill="black")

        # Draw country (BONUS)
        if self.country != None:
            self.canvas.create_text(self.canvas.winfo_width() / 2, country_y, text=f"Country: {country}", font=("Arial", line_width*7), fill="black")

    # Check sum Function
    def checksum(self, code):
        odd_sum = 0
        even_sum = 0
        for i in range(len(code)):
            if i % 2 == 0:
                odd_sum += int(code[i])
            else:
                even_sum += int(code[i])
        total = odd_sum + even_sum * 3
        check_digit = 10 - total % 10
        if check_digit == 10:
            check_digit = 0
        return str(check_digit)

# Main Function
def main():
    Barcode()

# Main
if __name__ == "__main__":
    main()