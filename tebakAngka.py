import tkinter as tk
import random

# Fungsi untuk memulai game
def mulai_game():
    global angka_acak, kesempatan
    angka_acak = random.randint(1, 100)  # Angka yang dipilih komputer
    kesempatan = 10  # Jumlah kesempatan menebak
    label_feedback.config(text="Tebak angka antara 1 dan 100.")
    entry_tebakan.config(state="normal")
    tombol_tebak.config(state="normal")
    tombol_reset.config(state="disabled")
    label_kesempatan.config(text=f"Kesempatan: {kesempatan}")

# Fungsi untuk mengecek tebakan pengguna
def tebak_angka():
    global kesempatan
    try:
        tebakan = int(entry_tebakan.get())
        if tebakan < 1 or tebakan > 100:
            label_feedback.config(text="Masukkan angka antara 1 dan 100.")
        else:
            kesempatan -= 1
            if tebakan < angka_acak:
                label_feedback.config(text="Tebakan terlalu kecil.")
            elif tebakan > angka_acak:
                label_feedback.config(text="Tebakan terlalu besar.")
            else:
                label_feedback.config(text=f"Selamat! Kamu berhasil menebak angka {angka_acak}!")
                entry_tebakan.config(state="disabled")
                tombol_tebak.config(state="disabled")
                tombol_reset.config(state="normal")
                return

            if kesempatan == 0:
                label_feedback.config(text=f"Kesempatan habis! Angka yang benar adalah {angka_acak}.")
                entry_tebakan.config(state="disabled")
                tombol_tebak.config(state="disabled")
                tombol_reset.config(state="normal")
            else:
                label_kesempatan.config(text=f"Kesempatan: {kesempatan}")
    except ValueError:
        label_feedback.config(text="Masukkan angka yang valid.")

# Fungsi untuk reset game
def reset_game():
    mulai_game()

# Setup jendela utama Tkinter
root = tk.Tk()
root.title("Game Tebak Angka")

# Label dan Entry untuk input tebakan
label_tebakan = tk.Label(root, text="Masukkan Tebakan (1-100):", font=("Arial", 14))
label_tebakan.pack(pady=10)

entry_tebakan = tk.Entry(root, font=("Arial", 14))
entry_tebakan.pack(pady=10)

# Tombol untuk menebak angka
tombol_tebak = tk.Button(root, text="Tebak", font=("Arial", 14), command=tebak_angka)
tombol_tebak.pack(pady=10)

# Label untuk feedback (apakah tebakan terlalu besar atau kecil)
label_feedback = tk.Label(root, text="Tebak angka antara 1 dan 100.", font=("Arial", 14))
label_feedback.pack(pady=10)

# Label untuk menampilkan sisa kesempatan
label_kesempatan = tk.Label(root, text="Kesempatan: 10", font=("Arial", 14))
label_kesempatan.pack(pady=10)

# Tombol untuk memulai ulang game
tombol_reset = tk.Button(root, text="Main Lagi", font=("Arial", 14), command=reset_game, state="disabled")
tombol_reset.pack(pady=10)

# Mulai game ketika aplikasi pertama kali dijalankan
mulai_game()

# Jalankan aplikasi Tkinter
root.mainloop()
