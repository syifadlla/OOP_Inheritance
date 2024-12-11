from animal import Animal

class karnivora(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, cara_berjalan, kemampuan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.cara_berjalan = cara_berjalan
        self.kemampuan = kemampuan

    def info_karnivora(self):
        super().info_animal()
        print('Cara Berjalan \t\t\t :', self.cara_berjalan,
              '\nKemampuan \t\t\t :', self.kemampuan)
        
harimau= karnivora('Harimau', 'Daging', 'Darat', 'Melahirkan', 'Berjalan', 'Bercakar tajam')
harimau.info_karnivora()
print('============================')
elang= karnivora('Elang', 'Daging', 'Udara', 'Bertelur', 'Terbang', 'Bercakar tajam')
elang.info_karnivora()
print('============================')
ular= karnivora('Ular', 'Daging', 'Darat', 'Bertelur', 'Melata', 'Berbisa')
ular.info_karnivora()

    
    

