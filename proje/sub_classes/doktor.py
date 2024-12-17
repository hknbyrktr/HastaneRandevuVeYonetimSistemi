from ..base_classes.base_class import BaseClass


class Doktor(BaseClass):

    def __init__(self, ad, brans,doktorlarData):
        super().__init__(ad,doktorlarData)
        self.brans = brans
        

    @classmethod
    def dosya_okuma(cls):
        
        try:
            with open("./proje/data/doktorlar.txt", "r", encoding="utf-8") as dosya:
                cls.doktorlarData = [satir.split(",") for satir in dosya]
            return cls.doktorlarData

        except FileNotFoundError:
            print("Dosya bulunamadı!")


    def randevuEkle(self, dr_indeks, zaman_indeks, randevu_zamani):
        
        if zaman_indeks == 0:                                                                  # eger saat_indeks'i 0 olarak bu metodu cagirirsak sona ekleme yapar
            self.doktorlarData[dr_indeks].append(randevu_zamani)    
        else:    
            self.doktorlarData[dr_indeks].insert(zaman_indeks, randevu_zamani)                 # doktorlarData guncelle
        
        self.veriyiYaz()                                      

    

    def randevuSil(self, dr_indeks, zaman_indeks):
         
        del self.doktorlarData[dr_indeks][zaman_indeks]                                        # Saat indeksini doktorun randevu saatlerinden sil

        self.veriyiYaz()




    def randevuDuzenle(self, dr_indeks, zaman_indeks, randevu_zamani):
     
        self.doktorlarData[dr_indeks][zaman_indeks] = randevu_zamani                           # degeri yerine koy 
        
        self.veriyiYaz() 


    def veriyiYaz(self):
        with open("./proje/data/doktorlar.txt", 'w', encoding='utf-8', newline='') as dosya:   # Güncellenmis doktorlarData'yi  yaz
            for doktor in self.doktorlarData:
                dosya.write(",".join(doktor))
