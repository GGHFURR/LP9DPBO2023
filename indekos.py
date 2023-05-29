from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni,jml_kamar,nama_penghuni,dayalistrik,image):
        self.jenis = "Indekos"
        self.image = image
        super().__init__(self.jenis, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.dayalistrik = dayalistrik
        self.nama_penghuni = nama_penghuni

    def get_image(self):
        return self.image
    
    def get_dayalistrik(self):
        return self.dayalistrik
    
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh : " + self.nama_penghuni + " dari : " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    # def get_summary(self):
    #     return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nNama Penghuni : " + self.nama_penghuni + "\n" + self.get_summary() + "Daya Listrik : " + str(self.dayalistrik) + "Watt\n" + self.get_dokumen() 