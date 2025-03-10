import tkinter as tk

# Fungsi untuk menambahkan angka ke tampilan
def tekan_tombol(angka):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(angka))

# Fungsi untuk operasi matematika
def hitung():
    try:
        ekspresi = entry.get()
        hasil = eval(ekspresi)
        entry.delete(0, tk.END)
        entry.insert(tk.END, hasil)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Fungsi untuk menghapus tampilan
def clear():
    entry.delete(0, tk.END)

# Setup jendela utama Tkinter
root = tk.Tk()
root.title("Kalkulator")

# Entry untuk menampilkan angka
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Tombol angka dan operasi
tombol_1 = tk.Button(root, text="1", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(1))
tombol_1.grid(row=1, column=0)

tombol_2 = tk.Button(root, text="2", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(2))
tombol_2.grid(row=1, column=1)

tombol_3 = tk.Button(root, text="3", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(3))
tombol_3.grid(row=1, column=2)

tombol_4 = tk.Button(root, text="4", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(4))
tombol_4.grid(row=2, column=0)

tombol_5 = tk.Button(root, text="5", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(5))
tombol_5.grid(row=2, column=1)

tombol_6 = tk.Button(root, text="6", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(6))
tombol_6.grid(row=2, column=2)

tombol_7 = tk.Button(root, text="7", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(7))
tombol_7.grid(row=3, column=0)

tombol_8 = tk.Button(root, text="8", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(8))
tombol_8.grid(row=3, column=1)

tombol_9 = tk.Button(root, text="9", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(9))
tombol_9.grid(row=3, column=2)

tombol_0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol(0))
tombol_0.grid(row=4, column=1)

# Tombol operasi
tombol_plus = tk.Button(root, text="+", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol('+'))
tombol_plus.grid(row=1, column=3)

tombol_minus = tk.Button(root, text="-", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol('-'))
tombol_minus.grid(row=2, column=3)

tombol_multiply = tk.Button(root, text="*", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol('*'))
tombol_multiply.grid(row=3, column=3)

tombol_divide = tk.Button(root, text="/", width=5, height=2, font=("Arial", 18), command=lambda: tekan_tombol('/'))
tombol_divide.grid(row=4, column=3)

# Tombol untuk menghitung hasil
tombol_equals = tk.Button(root, text="=", width=5, height=2, font=("Arial", 18), command=hitung)
tombol_equals.grid(row=4, column=2)

# Tombol untuk menghapus
tombol_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear)
tombol_clear.grid(row=5, column=0, columnspan=2, sticky="ew")

# Jalankan aplikasi Tkinter
root.mainloop()
