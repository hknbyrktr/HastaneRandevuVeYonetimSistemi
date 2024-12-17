from abc import ABC, abstractmethod
import time
import sys
import os


class BaseClass(ABC):

    def __init__(self, ad, doktorlarData = None, hastalarData = None, randevularData = None, personelData = None):
        self.ad = ad
        self.doktorlarData = doktorlarData
        self.hastalarData = hastalarData
        self.randevularData = randevularData
        self.personelData = personelData

    
    @classmethod
    def kayan_noktalar(cls, metin_1, metin_2):                                      # Animasyon fonksiyonu
        toplam_adim = 2
        for _ in range(toplam_adim):
            for i in range(4):
                sys.stdout.write("\r" + " " * 20)                       # Satırı temizle
                sys.stdout.write(f"\r{metin_1}" + "." * i)                # Noktaları ekle
                sys.stdout.flush()
                time.sleep(0.5)                                         # Her adımda 0.5 saniye bekle  
        
        print(f"\n{metin_2}")

        time.sleep(1)
        os.system('cls')                                                # ekranda 1sn gozuk sonra terminali temizle

    @classmethod
    def dosya_okuma(cls):
            
        try:                                                            # Dosyaları okumaya çalış hata verirse yakala 
            with open("./proje/data/doktorlar.txt", "r", encoding="utf-8") as dosya:
                
                cls.doktorlarData = [satir.split(",") for satir in dosya]
                
            with open("./proje/data/hastalar.txt", "r", encoding="utf-8") as dosya:
                cls.hastalarData = [satir.split(",") for satir in dosya]

            with open("./proje/data/personel.txt", "r", encoding="utf-8") as dosya:
                cls.personelData = [satir.split(",") for satir in dosya]
                
            with open("./proje/data/randevular.txt", "r", encoding="utf-8") as dosya:
                cls.randevularData = [satir.split(",") for satir in dosya]

            cls.kayan_noktalar("Sistem Yükleniyor","Sistem dosyaları içe aktarılı.")
            
            
            TF = True
            return TF, cls.doktorlarData, cls.hastalarData, cls.personelData, cls.randevularData


        except FileNotFoundError:                                           # Hata verirse yakala
            print("Dosya bulunamadı!")

            TorF = False
            return TorF 
        
    





