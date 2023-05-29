from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, dayalistrik,image):
        self.jenis = "Apartemen"
        self.image = image
        super().__init__(self.jenis, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.dayalistrik = dayalistrik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."
    
    def get_image(self):
        return self.image
    
    def get_dayalistrik(self):
        return self.dayalistrik
    
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n" + self.get_summary() + "Daya Listrik : " + str(self.dayalistrik) + "Watt\n" + self.get_dokumen() 