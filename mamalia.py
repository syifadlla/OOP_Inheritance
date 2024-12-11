from animal import Animal

class mamalia(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, kulit, ukuran):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.kulit = kulit
        self.ukuran = ukuran

    def info_mamalia(self):
        super().info_animal()
        print('Kulit \t\t\t\t :', self.kulit,
              '\nUkuran \t\t\t\t :', self.ukuran)
        
sapi= mamalia('Sapi', 'Daun', 'Darat', 'Melahirkan', 'Berbulu', 'Sedang')
sapi.info_mamalia()
print('=============================================')
gajah= mamalia('Gajah', 'Daun', 'Darat', 'Melahirkan', 'Sedikit berbulu', 'Besar')
gajah.info_mamalia()
print('=============================================')
kucing= mamalia('Kucing', 'Ikan', 'Darat', 'Melahirkan', 'Berbulu', 'Kecil')
kucing.info_mamalia()
    
    

