#berisi kontak untuk menjalankan program kontak

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()


    def melihat_kontak(self):
        # melihat kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' +item)
        else:
            print("Kontak masih kosong!!!")
            return 1 # jika kontak kosong akan retunr ke awal
    def menambah_kontak(self):
        # menambahkan kontak baru
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomer hp kontak yang baru: ")
        email = input("Masukkan email kontak yang baru: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # menghapus kontak

        if self.melihat_kontak() == 1:  #jika kontak kosong akan return ke awal
            return
        else:
            try:
                i_hapus = int(input("Masukkan nomer kontak yang akan dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud sudah dihapus!")
            except:
                print("input yang anda masukkan salah!")
    def keluar_kontak(self):
        dokumen.menyimpan_kontak(isi=self.kontak)
