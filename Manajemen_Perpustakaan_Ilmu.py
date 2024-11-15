class Buku:
    def __init__(self, judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku):
        self.__judul_buku = judul_buku
        self.__pengarang_buku = pengarang_buku
        self.__tahun_terbit = tahun_terbit
        self.__ISBN = ISBN
        self.__Status_buku = Status_buku
        
    def menampilkan_informasi_buku(self):
        print(f"Judul Buku: {self.__judul_buku}\nPengarang Buku: {self.__pengarang_buku}\nTahun Terbit: {self.__tahun_terbit}\nISBN: {self.__ISBN}\nStatus Buku: {self.__Status_buku}")
        
    def get_judul_buku(self):
        return self.__judul_buku
    
    def get_ISBN(self):
        return self.__ISBN
    
    def get_status_buku(self):
        return self.__Status_buku
    
    def set_status_buku(self, status_buku):
        self.__Status_buku = status_buku


class BukuNovel(Buku):
    def __init__(self, judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku, buku_nv):
        super().__init__(judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku)
        self.__buku_nv = buku_nv
        
    def get_kode_buku_nv(self):
        return self.__buku_nv
        
    def menampilkan_informasi_buku(self):
        super().menampilkan_informasi_buku()
        print(f"Buku Novel: {self.__buku_nv}")


class BukuPengetahuanUmum(Buku):
    def __init__(self, judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku, buku_pu):
        super().__init__(judul_buku, pengarang_buku, tahun_terbit, ISBN, Status_buku)
        self.__buku_pu = buku_pu
        
    def get_kode_buku_pu(self):
        return self.__buku_pu
        
    def menampilkan_informasi_buku(self):
        super().menampilkan_informasi_buku()
        print(f"Kode Buku Pengetahuan Umum: {self.__buku_pu}")


class Anggota:
    def __init__(self, nama_anggota_perpustakaan, nomor_anggota_perpustakaan, alamat):  
        self.__nama_anggota = nama_anggota_perpustakaan
        self.__nomor_anggota = nomor_anggota_perpustakaan
        self.__alamat = alamat
        self.__daftar_pinjaman = []
        
    def get_nama_anggota(self):
        return self.__nama_anggota
    
    def get_nomor_anggota(self):
        return self.__nomor_anggota
    
    def menampilkan_informasi_anggota(self):
        print(f"Nama Anggota: {self.__nama_anggota}\nNomor Anggota: {self.__nomor_anggota}\nAlamat: {self.__alamat}")
        
    def pinjam_buku(self, buku):
        if buku.get_status_buku() == "tersedia":
            self.__daftar_pinjaman.append(buku)
            buku.set_status_buku("dipinjam")
            print(f"Buku '{buku.get_judul_buku()}' berhasil dipinjam.")
        else:
            print(f"Mohon maaf, Buku '{buku.get_judul_buku()}' tidak tersedia.")
    
    def kembalikan_buku(self, buku):
        if buku in self.__daftar_pinjaman:
            self.__daftar_pinjaman.remove(buku)
            buku.set_status_buku("tersedia")
            print(f"Buku '{buku.get_judul_buku()}' berhasil dikembalikan.")
        else:
            print(f"Buku '{buku.get_judul_buku()}' tidak ada dalam daftar pinjaman.")


class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []
        self.__daftar_anggota = []
        
    def menambahkan_buku(self, buku):
        self.__daftar_buku.append(buku)
        print(f"Buku '{buku.get_judul_buku()}' berhasil ditambahkan.")
        
    def menambahkan_anggota_baru(self, nama_anggota, nomor_anggota, alamat):
        anggota_baru = Anggota(nama_anggota, nomor_anggota, alamat)
        self.__daftar_anggota.append(anggota_baru)
        print(f"Anggota '{anggota_baru.get_nama_anggota()}' berhasil ditambahkan.")
            
    def pinjam_buku(self, nomor_anggota, ISBN):
        anggota = next((anggota for anggota in self.__daftar_anggota if anggota.get_nomor_anggota() == nomor_anggota), None)
        buku = next((buku for buku in self.__daftar_buku if buku.get_ISBN() == ISBN), None)
        
        if anggota and buku:
            anggota.pinjam_buku(buku)
        else:
            print("Buku atau anggota tidak valid!")
    
    def kembalikan_buku(self, nomor_anggota, ISBN):
        anggota = next((anggota for anggota in self.__daftar_anggota if anggota.get_nomor_anggota() == nomor_anggota), None)
        buku = next((buku for buku in self.__daftar_buku if buku.get_ISBN() == ISBN), None)
        
        if anggota and buku:
            anggota.kembalikan_buku(buku)
        else:
            print("Buku atau anggota tidak valid!")

    def menampilkan_daftar_buku(self):
        print("Daftar Buku Tersedia di Perpustakaan Ilmu:")
        for buku in self.__daftar_buku:
            if buku.get_status_buku() == "tersedia":
                buku.menampilkan_informasi_buku()
                print("\n" + "-" * 30 + "\n")
    
    def menampilkan_informasi_anggota(self):
        for anggota in self.__daftar_anggota:
            anggota.menampilkan_informasi_anggota()
            print("\n" + "-" * 30 + "\n")


def menu(perpustakaan):
    print("----------------------------------------------------------------------")
    print("-----------------SELAMAT DATANG DI PERPUSTAKAAN ILMU------------------")
    print("----------------------------------------------------------------------")
    print("\n")
        
    while True:
        print("Menu Perpustakaan Ilmu:")
        print("1. Informasi Buku Perpustakaan Ilmu")
        print("2. Tambah Buku")
        print("3. Tambah Anggota")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Daftar Buku Tersedia")
        print("7. Informasi Anggota Perpustakaan Ilmu")
        print("8. Keluar")
        
        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            perpustakaan.menampilkan_daftar_buku()
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "2":
            print("Masukkan informasi buku:")
            print("Pilih jenis buku:")
            print("1. Buku Pengetahuan Umum")
            print("2. Buku Novel")
            jenis_buku = input("Pilih (1/2): ")
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            tahun = input("Masukkan tahun terbit: ")
            ISBN = input("Masukkan ISBN: ")
            if jenis_buku == "1":
                kode_buku_pu = input("Masukkan Kode buku Pengetahuan Umum: ")
                buku = BukuPengetahuanUmum(judul, pengarang, tahun, ISBN, "tersedia", kode_buku_pu)
            elif jenis_buku == "2":
                kode_buku_nv = input("Masukkan Kode buku Novel: ")
                buku = BukuNovel(judul, pengarang, tahun, ISBN, "tersedia", kode_buku_nv)
                
            perpustakaan.menambahkan_buku(buku)
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "3":
            nama = input("Masukkan nama anggota: ")
            nomor = input("Masukkan nomor anggota: ")
            alamat = input("Masukkan alamat anggota: ")
            perpustakaan.menambahkan_anggota_baru(nama, nomor, alamat)
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "4":
            nomor_anggota = input("Masukkan nomor anggota: ")
            ISBN = input("Masukkan ISBN buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(nomor_anggota, ISBN)
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "5":
            nomor_anggota = input("Masukkan nomor anggota: ")
            ISBN = input("Masukkan ISBN buku yang ingin dikembalikan: ")
            perpustakaan.kembalikan_buku(nomor_anggota, ISBN)
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "6":
            perpustakaan.menampilkan_daftar_buku()
            print("\n" + "-" * 30 + "\n")
            input("Tekan Enter untuk melanjutkan...")
        elif pilihan == "7":
            perpustakaan.menampilkan_informasi_anggota()
            print("\n" + "-" * 30 + "\n")
            input("--Tekan Enter untuk melanjutkan!--")
        elif pilihan == "8":
            print("--Terima kasih telah berkunjung di perpustakaan ilmu--")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")

if __name__ == "__main__":
    perpustakaan = Perpustakaan()            
    menu(perpustakaan)

            
