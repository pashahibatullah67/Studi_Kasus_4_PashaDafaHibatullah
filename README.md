# Studi_Kasus_4_PashaDafaHibatullah

Nama: Pasha Dafa Hibatullah
Nim: 067
Kelas: B

Halo semuanya, pada kesempatan kali ini saya akan menjelaskan tentang studi kasus 5 yang dimana kita telah mempelajari yang namanya definition DLL. Studi kasus saya kali ini adalah program perhitungan biaya pemesanan kamar hotel mulai dari jenis kaamar hingga lama menginapnya. Program ini menggunakan function, percabanagan, perulangan, return, hingga proses perhtungan untuk menentukan total biaya kamar yang harus dibayar. Didialamnnya pengguna dapat memilih tipe atau jenis kamar dan juga seberapa lama ia akan menginap, kemudian program akan menampilkan total biaya berdasarkan tarif kamar yang dipilih. Dan tanpa berlama-lama, mari kita masuk ke dalam masing-masing penjelasan.

<img width="344" height="20" alt="Screenshot 2026-09-23 180553" src="https://github.com/user-attachments/assets/59010595-6d8c-4f65-a966-0e34ce199e26" />

Kode diatas merupakan kode yang digunakan untuk membuat function hitung_biaya() dengan dua parameter di dalamnya, yaitu tipe_kamar yang digunakan untuk menentukan tipe kamar dan lama_menginap digunakan untuk menentukan jumlah malam menginap.

<img width="266" height="67" alt="Screenshot 2026-09-23 181246" src="https://github.com/user-attachments/assets/1b912827-d8b8-4a45-b4bb-7eb4de5a548f" />

Bagian ini adalah bagian yang dipakai untuk mengecek tipe kamar yang akan dipilih oleh pengguna. Seperti contohnya, jika pengguna memilih tipe kamar standard. Jika iya, maka tarif yang akan ditetapkan permalam adalah Rp. 200.000.00 per malam. Dan jika pengguna memilih tipe kamar deluxe, maka tarif yang akan ditetapkan adalah Rp. 350.000.00 per malam.

<img width="389" height="62" alt="Screenshot 2026-09-23 181900" src="https://github.com/user-attachments/assets/37e86717-153d-4de8-9a3f-7237223d5fcb" />

Kode diatas merupakan kode yang digunakan untuk menghitung total biaya berdasarkan tarif kamar dan lama menginap. Setelah total biaya sudah didapatkan, maka return total mengembalikakn hasil perhitungan tersebut dari function.

<img width="477" height="85" alt="Screenshot 2026-09-23 182645" src="https://github.com/user-attachments/assets/ff2f9b91-cc30-44b9-8a00-ce2dfc06c02a" />

Pada bagian ini, while True digunakan untuk membuat menu pilihan kamar terus ditampilkan sampai pengguna memilih pilihan yang diinginkan. Yang dimana, menu didalamnya berisikan pilihan kamar standard, deluxe, hingga pilihan untuk pengguna membatalkan pemesanan.

<img width="480" height="199" alt="Screenshot 2026-09-23 183113" src="https://github.com/user-attachments/assets/0d9c4927-e0f8-4e13-96ad-34cf69a2825d" />

Kode ini digunakan untuk memproses pilihan kamar yang telah dimasukkan oleh pengguna. Jika pengguna memilih 1. maka program akan memilih tipe kamar standard. Sedangkan jika pengguna memilih nomor 2. maka program akan memilih tipe kamar deluxe. Pilihan 3. digunakan jika pengguna ingin membatalkan pemesanan kamar, dan jika pengguna memilih pilihan yang tidak ada, maka program akan memberi pesan bawha pilihan sang pengguna tidak valid dan meminta pengguna untuk kembali. Break digunakan untuk menghentikan yang namanya perulangan setelah pengguna telah memilih kamar yang di tentukan.

<img width="461" height="76" alt="Screenshot 2026-09-23 183821" src="https://github.com/user-attachments/assets/ba82752c-53a4-48db-b4fc-86f0b37ab363" />

Kode pertama pada bagian ini digunakan untuk meminta pengguna memasukkan jumlah malam selama menginap di hotel. Fungsi int() digunakan supaya input yang dimasukkan berupa angka dan dapat digunakan dalam perhitungan. Setelah itu hitung_biaya dipanggil dengan memasukkan tipe_kamar dan lama_menginap sebagai parameter untuk mendapatkan hasil total biaya pemesanan.

<img width="461" height="75" alt="Screenshot 2026-09-23 184557" src="https://github.com/user-attachments/assets/f2f3509e-8b71-44dc-9bca-70898db7ffad" />

Kode ini digunakan untuk menampilkan hasil akhir dari pemesanan hotel. Program akan menampilkan tipe kamar yang dipilih pengguna, jumlah malam menginap di hotel tersebut, dan juga total biaya yang harus dibayar berdasarkan hasil perhitungan sebelumnya.

<img width="412" height="140" alt="Screenshot 2026-09-23 184851" src="https://github.com/user-attachments/assets/a2486d88-07ee-4cba-b296-f82ed4f46b62" />

Output diatas tersebut menunjukkan proses pemesanan mulai dari awal memilih tipe kamar yang diinginkan hingga sampai hasil akhir. Sepeerti contohnya diatas, pengguna memilih kamar deluxe yang memiliki harga baiaya Rp. 350.000.00 per malam dan menginap selama 3 malam. Program kemudian menghitung dan menampilkan total biaya sebesar Rp. 1.050.000.00 yang pengguna harus bayar
