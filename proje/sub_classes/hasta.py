from ..base_classes.base_class import BaseClass 
from .doktor import Doktor as D
import time
import os


class Hasta(BaseClass):


    def __init__(self, tc, ad, soyad, sifre, tibbiGecmis, doktorlarData, hastalarData, randevularData):
        super().__init__(ad, doktorlarData, hastalarData, randevularData,None)                  # BaseClass'a parametreleri geçiyoruz
        self.tc = tc  
        self.soyad = soyad
        self.sifre = sifre
        self.tibbiGecmis = tibbiGecmis

    def hastaMenusu(self):                                                                      # Kisi hasta sekmesine girdiyse burdan devam edicek.

        dongu = True
        while True:
            time.sleep(0.5)
            os.system('cls')                                                                    # ekranda 0.5sn gozuk sonra terminali temizle
            
            print("********************************************************************")
            print("*                                                                  *")
            print("*                        HASTA PANELİ                              *")
            print("*                                                                  *")
            print("********************************************************************")
            print()
            print()
            print("**********************************************")
            print("* 1- Randevu alma ve iptal etme.             *")
            print("* 2- Mevcut randevuları görüntüleme.         *")
            print("* 3- Tıbbi geçmişi görüntüleme               *")
            print("* 00- Ana Safya Dön                          *")
            print("* 0- Çıkış Yap                               *")
            print("**********************************************")
            print()
            secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")
            print("-----------------------------------------")
            time.sleep(0.5)
            os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle
            if(secim == "1"):
                while True:
                    time.sleep(0.5)
                    os.system('cls')                                                                    # ekranda 0.5sn gozuk sonra terminali temizle
                    print()
                    print("**********************************************")
                    print("*    Randevu Alma Ve İptal Etme  Paneli      *")
                    print("**********************************************")
                    print()
                    print("**********************************************")
                    print("* 1- Randevu alma                            *")
                    print("* 2- Randevu iptal etme                      *")
                    print("* 00- Geri Dön                               *")
                    print("* 0- Çıkış yap                               *")
                    print("**********************************************")
                    print()

                    secim_1 = input("Lütfen yapmak istediğiniz işlemi seçin: ")
                    print("-----------------------------------------")
                    
                    time.sleep(0.5)
                    os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle
                    
                    if(secim_1 == "1"):                                                          # -- Randevu alma --

                        while True:                                                            # Atanmamis deger girildiyse tekrarla
                            print()
                            print("**********************************************")
                            print("*           Randevu Alma Paneli              *")
                            print("**********************************************")
                            print()        
                            print("**********************************************")
                            print("*      Randevu Alınıcak Polikılinikler       *")
                            print("*--------------------------------------------*")
                            print("*                                            *")
                            print("* 1- Kardiyoloji                             *")
                            print("* 2- Kulak Burun Boğaz                       *")
                            print("* 3- Optik                                   *")
                            print("* 4- Dahiliye                                *")
                            print("* 5- Nöroloji                                *")
                            print("* 6- Diyabet                                 *")
                            print("* 7- Göğüs Cerrahisi                         *")
                            print("* 8- Beslenme ve Diyetetik                   *")
                            print("* 9- Fizik Tedavi ve Rehabilitasyon          *")
                            print("* 10- Genel Cerrahi                          *")
                            print("*--------------------------------------------*")
                            print("* 00- Geri Dön                               *")
                            print("* 0- Çıkış yap                               *")
                            print("**********************************************")

                            secim_2 = input("Lütfen randevu almak istediğiniz polikinliği seçin: ")
                            print("-----------------------------------------------------")

                            time.sleep(0.5)
                            os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle

                            if secim_2 in ("00","0","1","2","3","4","5","6","7","8","9","10"):                          # Dogru deger girildimi kontrol
                                break

                            print("Lütfen doğru bir değer girin !!! \n")


                        dr_indeks = "Seçilmedi"
                        if(secim_2 == "1"):
                            dr_indeks = self.doktorAra("Kardiyoloji")
                        elif(secim_2 == "2"):
                            dr_indeks = self.doktorAra("Kulak Burun Boğaz")
                        elif(secim_2 == "3"):
                            dr_indeks = self.doktorAra("Optik")
                        elif(secim_2 == "4"):
                            dr_indeks = self.doktorAra("Dahiliye")
                        elif(secim_2 == "5"):
                            dr_indeks = self.doktorAra("Nöroloji")
                        elif(secim_2 == "6"):
                            dr_indeks = self.doktorAra("Diyabet")
                        elif(secim_2 == "7"):
                            dr_indeks = self.doktorAra("Göğüs Cerrahisi")
                        elif(secim_2 == "8"):
                            dr_indeks = self.doktorAra("Beslenme ve Diyetetik")
                        elif(secim_2 == "9"):
                            dr_indeks = self.doktorAra("Fizik Tedavi ve Rehabilitasyon")
                        elif(secim_2 == "10"):
                            dr_indeks = self.doktorAra("Genel Cerrahi")
                        elif secim_2 == "00":
                            dongu = False
                            continue
                        elif(secim_2 == "0"):
                            exit()
                            
                        while True:
                            print(f"\n{self.doktorlarData[dr_indeks][1]} için;")
                            print("----------------------------")
                            i = 0
                            
                            if len(self.doktorlarData[dr_indeks]) > 3:
                                gun = self.doktorlarData[dr_indeks][3][:2]
                            
                            for zaman in self.doktorlarData[dr_indeks][3:]:                        # Secilen doktorun bostaki randevularini yaz
                                
                                if zaman[:2] != gun:
                                    print("----------------------------")
                                    gun = zaman[:2]
                                
                                i+=1
                                print(f" {i}- {zaman}")
                            
                            if i == 0:
                                print("Randevu bulunmamaktadır!")
                            print("------------")
                            print("0- Çıkış Yap")

                            zaman_indeks = str(int(input("Randevu seçiniz: ")) + 2)                    # dogru indeksi bulmak icin -1 yapmaklıyız ama -
                                                                                                   # zamanlar 3. indeksten basliyor (3-1=2) bu yüzden +2 ekle
                            
                            if zaman_indeks == "2":                                                  # aslinda burada 0' a basti 
                                exit()

                            for j in range(3, i+3):                                                # Yanlis deger secilmemesi icin kontrol
                                if zaman_indeks == str(j):
                                    loop = True
                                
                            
                            if loop:
                                break        

                            print("Lütfen doğru bir değer girin !!!\n")
                                    
                        self.kayan_noktalar("İşleminiz gerçekleştiriliyor","Randevunuz onaylanmıştır.")
                        
                        
                        doktor = D(self.doktorlarData[dr_indeks][1],self.doktorlarData[dr_indeks][2],self.doktorlarData)
                        print(self.doktorlarData[dr_indeks][int(zaman_indeks)])

                        tarih,saat = str(self.doktorlarData[dr_indeks][int(zaman_indeks)]).split("/")      # randevular.txt' e eklenecek yeni satiri olustur.
                        yeni_satir = f"{self.tc}, {self.doktorlarData[dr_indeks][0]}, {self.doktorlarData[dr_indeks][1]}, {tarih}, {saat}, beklemede "
                    
                        self.randevuEkle(yeni_satir)                                           # randevular.txt' e yeni randevuyu ekle

                        doktor.randevuSil(dr_indeks,int(zaman_indeks))                           # doktor.txt' i guncelle


                        print("İşleminiz tamamlandı hasta paneline yönlendiriliyorsunuz.")

                        time.sleep(0.5)
                        os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle
                        break

                    


                    elif(secim_1 == "2"):                                                        # -- Randevu iptal etme --
                        
                        print()
                        print("**********************************************")
                        print("*         Randevu İptal Etme Paneli          *")
                        print("**********************************************")
                        print()
                        print("\nRandevularınız;")

                        while True:
                            
                            sira,sozluk = self.randevuGoster()
                            
                            secim = input("\nİptal etmek istediğiniz randevuyu seçin: ")
                            
                            if secim == "00":
                                dongu = False
                                break
                            elif secim == "0":
                                exit()

                            dongu = False
                            for j in range(sira+1):                                            # Yanlis deger secilmemesi icin kontrol
                                if secim == str(j):
                                    self.randevuSil(sozluk[int(secim)])
                                    self.kayan_noktalar("İşleminiz gerçekleştiriliyor","Randevunuz İptal Edildi.")
                                    dongu = True
                                
                            if(dongu):
                                break

                            print("Lütfen doğru bir değer girin !!!\n")
                        
                                        

                    elif(secim_1 == "00"):
                        break
                    
                    elif(secim_1 == "0"):                                                    # -- Cikis yap --
                        exit()

                    else:   
                        if dongu:                                                                   # -- Yanlis karakter secildi --
                            print("Lütfen doğru bir değer girin !!!\n")


            elif(secim == "2"):                                                          # -- Mevcut randevuları görüntüleme --
                
                print()
                print("**********************************************")
                print("*                                            *")
                print("*         Mecvut Randevularınız              *")
                print("*                                            *")
                print("**********************************************")
                print()

                self.randevuGoster()
                
                while True: 
                    a = input("Seçiniz: ")
                    print("-----------")
                    if a== "00":
                        break
                    elif a == "0":
                        exit()
                    print("\nLütfen doğru bir değer girin !!!\n")



            elif(secim == "3"):                                                          # Tıbbi geçmişi görüntüleme  
                print()
                print("**********************************************")
                print("*    Tıbbi Geçmişi Görüntüleme Paneli        *")
                print("**********************************************")
                print()
                
                print("\n Tıbbi Geçmişiniz;")
                print("      Tarih      /     Saat     /     Hastalık")
                print("------------------------------------------------")
                satir = 0
                for hasta in self.hastalarData[1:]:
                    
                    if len(hasta) > 1:                                                # bos satir almamasi icin
                        if hasta[0] == self.tc:
                            satir +=1
                            
                            adet = hasta[4].split("#")

                            for adet_1 in adet:
                                tarih,saat,hastalik = adet_1.split("/")

                            print(f"{satir}-  {tarih:<20}  /  {saat:<19}  /  {hastalik}")
                while True:
                    print("--------------------------")
                    print("00- Geri Dön ")
                    print("0- Çıkış Yap")
                    secim_1 = input("Seçiniz: ")
                    print("------------")

                    if secim_1 == "00":
                        break
                    if secim_1 == "0":
                        exit()
                    print("Lütfen doğru bir değer girin !!!\n")


            
            elif(secim == "00"):                                                          # Ana sayfaya don
                return False
            elif(secim == "0"):
                exit()
            else:                                                                      # Yanlis karakter secildi
                    print("Hatalı seçim, tekrar deneyin.")
      
    


    
    def doktorAra(self,brans):
        while True:
            
            print("\n     Doktorun Adı         /       Branşı")
            print("--------------------------------------------")
            sira = 0
            i = 0
            sozluk = {}
            for doktor in self.doktorlarData[1:]:                                     # Hastanın aradigi brasta doktor varmi diye kontrol ediyoruz
                
                i += 1
                if len(doktor) > 1:                                                   # bos satir varsa atla
                    if doktor[2] == brans:
                        
                        sira += 1
                        sozluk[sira] = i                                              # brans' a gore siralama yaptigimiz icin hangi doktoru sectigimizi karistirmayalim

                        print(f"{sira}- {doktor[1]:<20}  /  {doktor[2]}   ")
            
            if sira == 0:
                print()
                print("*******************************************************")
                print("*  Üzgünüm bu branşa ait doktorumuz bulunmamaktadır!  *")
                print("*******************************************************")
                print()
            print("\n------------")
            print("0- Çıkış Yap")
            secim = input("\nRadevu almak istediğiniz doktoru seçin: ")
            
            if secim == "0":
                    exit()
            for j in range(1,sira+1):                                                   # Yanlis deger secilmemesi icin kontrol
                if secim == str(j):
                    return sozluk[int(secim)]                                              # doktorlarData daki dogru indeks'i geri donduruyoruz 
                


            print("Lütfen doğru bir değer girin !!!\n")


    def randevuGoster(self):

        print("   Dr ID  /       Doktor Adı       /  Randevu Tarihi  /   Randevu Saati  /  Durum")
        print("---------------------------------------------------------------------------------------")

        sira = 0
        i = 0
        sozluk = {}
        for randevu in self.randevularData[1:]:                            # Hastanın aradigi brasta doktor varmi diye kontrol ediyoruz
            
            i += 1
            if len(randevu) > 1:                                           # Bos satir varsa atla
                if randevu[0] == self.tc:
                    
                    sira += 1
                    sozluk[sira] = i                                       # kisinin kendi randevularini gosterecegimizden sira ile indeks karismamasi icin

                    print(f"{sira}- {randevu[1]:<5}  /  {randevu[2]:20}  /  {randevu[3]:14}  /  {randevu[4]:15} /  {randevu[5]}")
        
        print("-----------------------")
        print("\n00- Geri Dön ")
        print("0- Çıkış Yap")

        return sira,sozluk
                    




    @staticmethod
    def kullanici_dogrula(tc, sifre,hastalarData):
        
        for hasta in hastalarData[1:]:
            
            if (hasta[0] == tc and hasta[3] == sifre):
                return True,hasta
        
        return False , None

        


    @classmethod
    def dosya_okuma(cls):
        
        try:
            with open("./proje/data/hastalar.txt", "r", encoding="utf-8") as dosya:
                cls.hastalarData = [satir.split(",") for satir in dosya]
            return cls.hastalarData

        except FileNotFoundError:
            print("Dosya bulunamadı!")


    def randevuEkle(self, yeni_satir): 
        
        with open("./proje/data/randevular.txt", 'a', encoding='utf-8', newline='') as dosya:
            dosya.write(yeni_satir) 

        # randevularData listesine ekle
        yeni_veri = yeni_satir.split(",")                                                       # Satiri virgule gore bolerek liste formatina donustur
        self.randevularData.append(yeni_veri)                          


    def randevuSil(self,silincek_satir):
        
        del self.randevularData[silincek_satir]

        with open("./proje/data/randevular.txt", 'w', encoding='utf-8', newline='') as dosya:    # Guncellenmis randevularData'ya yaz
            for randevu in self.randevularData:
                dosya.write(",".join(randevu))

