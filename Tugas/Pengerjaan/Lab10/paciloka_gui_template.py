import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'], 'hotel2': [12, 500000, 'kode_hotel_2'], 'hotel3': [10, 7500000, 'kode_hotel_3'], 
                        'hotel4': [1, 1000000, 'kode_hotel_4'], 'hotel5': [10, 900000, 'kode_hotel_5'], 'hotel6': [10, 6000000, 'kode_hotel_6']}
        
        # TODO : tambahkan title dan ukuran windows
        self.homepage()
        
    # TODO : tambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        pass
    
    # TODO : tambahkan logic untuk validasi proses booking
    def booking(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
