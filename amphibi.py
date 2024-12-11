from animal import Animal

class Amphibi(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal()
        print('Jenis air \t\t\t :', self.jenis_air,
              '\nBernapas \t\t\t :', self.bernapas)
        
katak= Amphibi('Katak', 'Serangga', 'Dua Alam', 'Bertelur', 'Air tawar', 'Kulit dan Paru-paru')
katak.info_amphibi()
print('===============================================')
salamender= Amphibi('Salamander', 'Serangga', 'Dua Alam', 'Bertelur', 'Air tawar', 'Insang, Kulit dan Paru-paru')
salamender.info_amphibi()
print('===============================================')
axolotl= Amphibi('Axolotl', 'Serangga', 'Dua Alam', 'Bertelur', 'Air tawar', 'Insang, Kulit dan Paru-paru')
axolotl.info_amphibi()
    
    

