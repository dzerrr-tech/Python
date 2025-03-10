import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambah produk
def tambah_barang():
    try:
        nama = entry_nama.get()  # Nama produk
        harga = float(entry_harga.get())  # Harga produk
        jumlah = int(entry_jumlah.get())  # Jumlah produk

        if nama == "" or harga <= 0 or jumlah <= 0:
            messagebox.showerror("Input Error", "Masukkan data produk yang valid!")
            return

        # Menambahkan ke list produk
        total_harga = harga * jumlah
        list_produk.insert(tk.END, f"{nama} - {jumlah} x {harga} = {total_harga}")
        daftar_produk.append({"nama": nama, "harga": harga, "jumlah": jumlah, "total": total_harga})
        
        # Mengosongkan field input
        entry_nama.delete(0, tk.END)
        entry_harga.delete(0, tk.END)
        entry_jumlah.delete(0, tk.END)
        
        hitung_total()  # Hitung total setelah menambahkan produk
    except ValueError:
        messagebox.showerror("Input Error", "Harga dan jumlah harus berupa angka!")

# Fungsi untuk menghitung total belanja
def hitung_total():
    total = sum(item["total"] for item in daftar_produk)
    
    # Menghitung diskon
    diskon_persen = float(entry_diskon.get()) if entry_diskon.get() else 0
    diskon = total * (diskon_persen / 100)
    
    # Menghitung pajak
    pajak_persen = float(entry_pajak.get()) if entry_pajak.get() else 0
    pajak = total * (pajak_persen / 100)
    
    # Total yang harus dibayar
    total_setelah_diskon = total - diskon
    total_akhir = total_setelah_diskon + pajak

    # Menampilkan total
    label_total.config(text=f"Total: {total:.2f}")
    label_diskon.config(text=f"Diskon ({diskon_persen}%): {diskon:.2f}")
    label_pajak.config(text=f"Pajak ({pajak_persen}%): {pajak:.2f}")
    label_total_bayar.config(text=f"Total yang harus dibayar: {total_akhir:.2f}")

# Fungsi untuk reset daftar belanja
def reset():
    daftar_produk.clear()
    list_produk.delete(0, tk.END)
    label_total.config(text="Total: 0.00")
    label_diskon.config(text="Diskon: 0.00")
    label_pajak.config(text="Pajak: 0.00")
    label_total_bayar.config(text="Total yang harus dibayar: 0.00")
    entry_diskon.delete(0, tk.END)
    entry_pajak.delete(0, tk.END)

# Daftar produk
daftar_produk = []

# Setup jendela utama Tkinter
root = tk.Tk()
root.title("Aplikasi Kasir")

# Label dan Entry untuk nama produk, harga, dan jumlah
label_nama = tk.Label(root, text="Nama Produk:")
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

label_harga = tk.Label(root, text="Harga Produk:")
label_harga.grid(row=1, column=0, padx=10, pady=10)
entry_harga = tk.Entry(root)
entry_harga.grid(row=1, column=1, padx=10, pady=10)

label_jumlah = tk.Label(root, text="Jumlah Produk:")
label_jumlah.grid(row=2, column=0, padx=10, pady=10)
entry_jumlah = tk.Entry(root)
entry_jumlah.grid(row=2, column=1, padx=10, pady=10)

# Tombol untuk menambah produk
tombol_tambah = tk.Button(root, text="Tambah Produk", command=tambah_barang)
tombol_tambah.grid(row=3, column=0, columnspan=2, pady=10)

# Listbox untuk menampilkan daftar produk
list_produk = tk.Listbox(root, height=10, width=40)
list_produk.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Label untuk diskon dan pajak
label_diskon = tk.Label(root, text="Diskon (%):")
label_diskon.grid(row=5, column=0, padx=10, pady=10)
entry_diskon = tk.Entry(root)
entry_diskon.grid(row=5, column=1, padx=10, pady=10)

label_pajak = tk.Label(root, text="Pajak (%):")
label_pajak.grid(row=6, column=0, padx=10, pady=10)
entry_pajak = tk.Entry(root)
entry_pajak.grid(row=6, column=1, padx=10, pady=10)

# Tombol untuk reset (posisi di bawah kanan)
tombol_reset = tk.Button(root, text="Reset", command=reset)
tombol_reset.grid(row=7, column=1, pady=10, sticky='e')  # sticky='e' agar berada di kanan

# Label untuk menampilkan total
label_total = tk.Label(root, text="Total: 0.00")
label_total.grid(row=8, column=0, padx=10, pady=10)

label_diskon = tk.Label(root, text="Diskon: 0.00")
label_diskon.grid(row=9, column=0, padx=10, pady=10)

label_pajak = tk.Label(root, text="Pajak: 0.00")
label_pajak.grid(row=10, column=0, padx=10, pady=10)

label_total_bayar = tk.Label(root, text="Total yang harus dibayar: 0.00")
label_total_bayar.grid(row=11, column=0, padx=10, pady=10)

# Jalankan aplikasi Tkinter
root.mainloop()
