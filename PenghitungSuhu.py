import tkinter as tk

# Fungsi untuk mengonversi suhu
def konversi_suhu():
    try:
        suhu_input = float(entry_suhu.get())  # Ambil input suhu
        dari_suhu = var_dari_suhu.get()  # Pilihan suhu input (Celsius, Fahrenheit, Kelvin)
        ke_suhu = var_ke_suhu.get()  # Pilihan suhu tujuan (Celsius, Fahrenheit, Kelvin)

        if dari_suhu == ke_suhu:
            label_hasil.config(text=f"Hasil konversi: {suhu_input} {suhu_nama[ke_suhu]}")
            return

        if dari_suhu == 0:  # Celsius
            if ke_suhu == 1:  # Konversi ke Fahrenheit
                hasil = (suhu_input * 9/5) + 32
                label_hasil.config(text=f"Hasil konversi: {hasil:.2f} °F")
            elif ke_suhu == 2:  # Konversi ke Kelvin
                hasil = suhu_input + 273.15
                label_hasil.config(text=f"Hasil konversi: {hasil:.2f} K")

        elif dari_suhu == 1:  # Fahrenheit
            if ke_suhu == 0:  # Konversi ke Celsius
                hasil = (suhu_input - 32) * 5/9
                label_hasil.config(text=f"Hasil konversi: {hasil:.2f} °C")
            elif ke_suhu == 2:  # Konversi ke Kelvin
                hasil = (suhu_input - 32) * 5/9 + 273.15
                label_hasil.config(text=f"Hasil konversi: {hasil:.2f} K")

        elif dari_suhu == 2:  # Kelvin
            if ke_suhu == 0:  # Konversi ke Celsius
                hasil = suhu_input - 273.15
                label_hasil.config(text=f"Hasil konversi: {hasil:.2f} °C")
            elif ke_suhu == 1:  # Konversi ke Fahrenheit
                hasil = (suhu_input - 273.15) * 9/5 + 32
                label_hasil.config(text=f"Hasil konversi: {hasil:.2f} °F")

    except ValueError:
        label_hasil.config(text="Masukkan nilai suhu yang valid!")

# Setup jendela utama Tkinter
root = tk.Tk()
root.title("Pengatur Suhu")

# Nama satuan suhu
suhu_nama = {0: "°C", 1: "°F", 2: "K"}

# Label untuk petunjuk
label_suhu = tk.Label(root, text="Masukkan suhu yang ingin dikonversi:")
label_suhu.pack()

# Entry untuk input suhu
entry_suhu = tk.Entry(root)
entry_suhu.pack()

# Pilihan untuk suhu input (Celsius, Fahrenheit, Kelvin)
label_dari_suhu = tk.Label(root, text="Pilih satuan suhu yang dimasukkan:")
label_dari_suhu.pack()

var_dari_suhu = tk.IntVar()

radio_celsius = tk.Radiobutton(root, text="Celsius", variable=var_dari_suhu, value=0)
radio_celsius.pack()

radio_fahrenheit = tk.Radiobutton(root, text="Fahrenheit", variable=var_dari_suhu, value=1)
radio_fahrenheit.pack()

radio_kelvin = tk.Radiobutton(root, text="Kelvin", variable=var_dari_suhu, value=2)
radio_kelvin.pack()

# Pilihan untuk suhu tujuan (Celsius, Fahrenheit, Kelvin)
label_ke_suhu = tk.Label(root, text="Pilih satuan suhu tujuan:")
label_ke_suhu.pack()

var_ke_suhu = tk.IntVar()

radio_celsius2 = tk.Radiobutton(root, text="Celsius", variable=var_ke_suhu, value=0)
radio_celsius2.pack()

radio_fahrenheit2 = tk.Radiobutton(root, text="Fahrenheit", variable=var_ke_suhu, value=1)
radio_fahrenheit2.pack()

radio_kelvin2 = tk.Radiobutton(root, text="Kelvin", variable=var_ke_suhu, value=2)
radio_kelvin2.pack()

# Tombol untuk melakukan konversi
tombol_konversi = tk.Button(root, text="Konversi", command=konversi_suhu)
tombol_konversi.pack()

# Label untuk menampilkan hasil konversi
label_hasil = tk.Label(root, text="Hasil konversi akan muncul di sini.")
label_hasil.pack()

# Jalankan aplikasi Tkinter
root.mainloop()
