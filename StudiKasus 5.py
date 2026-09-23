def hitung_biaya (tipe_kamar, lama_menginap):
    if tipe_kamar == "Standard":
        biaya_kamar_per_malam = 200000
    elif tipe_kamar == "Deluxe":
        biaya_kamar_per_malam = 350000

    total_biaya = biaya_kamar_per_malam * lama_menginap
    return total_biaya

while True:
    print("=== PEMESANAN KAMAR HOTEL ===")
    print("1. Kamar Standard (Rp 200.000/malam)")
    print("2. Kamar Deluxe (Rp 350.000/malam)")
    print("3. Batalkan Pemesanan")

    pilihan = input("Masukkan pilihan tipe kamar (1/2/3): ")

    if pilihan == "1":
        tipe_kamar = "Standard"
        break
    elif pilihan == "2":
        tipe_kamar = "Deluxe"
        break
    elif pilihan == "3":
        print("Pemesanan berhasil dibatalkan.")
        exit()
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

lama_menginap = int(input("Masukkan lama menginap (dalam malam): "))

total_biaya = hitung_biaya(tipe_kamar, lama_menginap)

print("=== DATA PEMESANAN KAMAR HOTEL ===")
print("Tipe Kamar anda:", tipe_kamar)
print("Lama anda menginap:", lama_menginap, "malam")
print("Total biaya yang harus anda bayar: Rp", total_biaya)