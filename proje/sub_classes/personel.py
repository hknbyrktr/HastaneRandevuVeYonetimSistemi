from ..base_classes.base_class import BaseClass
from .doktor import Doktor as D
import time
import os

class Personel(BaseClass):

    def __init__(self, ad, sifre, gorev, doktorlarData, randevularData, personelData):
        super().__init__(ad, doktorlarData, None, randevularData, personelData)
        self.sifre = sifre
        self.gorev = gorev


    def personelMenusu(self):
        dongu = True
        while True:
            time.sleep(0.5)
            os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle
            print("********************************************************************")
            print("*                                                                  *")
            print("*                      PERSONEL PANELİ                             *")
            print("*                                                                  *")
            print("********************************************************************")
            print()
            print()
            print("***************************************************")
            print("* 1- Doktorların takvimlerini yönetme             *")
            print("* 2- Randevuları onaylama ya da iptal etme        *")
            print("* 3- Hasta bilgilerine erişim                     *")
            print("* 00- Ana Safya Dön                               *")
            print("* 0- Çıkış Yap                                    *")
            print("***************************************************")
            print()
            secim = input("Lütfen yapmak istediğiniz işlemi seçin: ")
            print("-----------------------------------------")
            time.sleep(0.5)
            os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle

            if secim == "1":                                                         # -- Doktorların takvimlerini yönetme --
                
                dongu = True
                while dongu:
                    print()
                    print("***************************************************")
                    print("*   Doktorların Takvimlerini Yönetme Paneli       *")
                    print("***************************************************")
                    print()
                    print("***************************************************")
                    print("* 1- Doktor takvimine randevu ekleme              *")
                    print("* 2- Doktor takviminden randevu çıkarma           *")
                    print("* 3- Doktor takvimini düzenleme                   *")
                    print("* 00- Geri Dön                                    *")
                    print("* 0- Çıkış Yap                                    *")
                    print("***************************************************")
                    print()
                    secim_1 = input("Lütfen yapmak istediğiniz işlemi seçin: ")
                    print("-----------------------------------------")

                    time.sleep(0.5)
                    os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle
                    if secim_1 == "1":                                              # -- Doktor takvimine randevu ekleme --
                        
                        while True:
                            print()
                            print("***************************************************")
                            print("*    Doktor Takvimine Randevu Ekleme Paneli       *")
                            print("***************************************************")
                            print()
                            
                            i, dr_indeks = self.doktorlariGoster()
                            if i == 0:
                                dongu = False
                                break

                            for j in range(1, i+1):                                   # dr_indeks degeri yanlis secilmemesi icin kontrol
                                
                                if int(dr_indeks) == j:
                                    
                                    i = self.randevuGoster(int(dr_indeks))

                                    print()
                                    print("******************************************************************************************************************************************")
                                    print("*                                                         DİKKAT!!! :                                                                    *")
                                    print("*----------------------------------------------------------------------------------------------------------------------------------------*")
                                    print("*- Gireceğiniz değer seçtiğiniz indeksin bulunduğu yere yazılacak olup, o indekste bulunan değerde bir sonraki indekse kayacaktır.       *")
                                    print("*- Fazladan girdiğiniz yada yanlış girdiğiniz bütün indeksler en sona eklenecektir.                                                      *")
                                    print("*- Yanlışlıkla girdiğiniz indeksler için 'Doktor takviminden randevu çıkarma paneli' ne gitmelisiniz.                                    *")
                                    print("*- Görüntülenecek randevu yoksa istediğiniz indeksi seçebilirsiniz direk sıraya olarak ekler.                                            *")
                                    print("******************************************************************************************************************************************")
                                    print()
                                    zaman_indeks = str(int(input("Sıra seçiniz: ")) + 2)                     # dogru indeksi bulmak icin -1 yapmaklıyız ama -
                                                                                                          # zamanlar 3. indeksten basliyor (3-1=2) bu yüzden +2 ekle.
                                    
                                    if zaman_indeks == "2":                                                 # aslinda burada 0' a basti 
                                        exit()

                                    loop = False
                                    doktor = D(self.doktorlarData[int(dr_indeks)][1],self.doktorlarData[int(dr_indeks)][2],self.doktorlarData)
                                    for j in range(3, i+3):                                               # Yanlis deger secilmemesi icin kontrol 
                                        if zaman_indeks == str(j):
                                            loop = True
                                        

                                    if not loop:
                                            zaman_indeks = "0"   

                                    print()
                                    print("******************************************************************************************************************************************")
                                    print("*                                                         DİKKAT!!! :                                                                    *")
                                    print("*----------------------------------------------------------------------------------------------------------------------------------------*")
                                    print("*- Gireceğiniz değeri yukarıdaki düzen doğrultusunda girmeye özen gösteriniz !                                                           *")
                                    print("*- Yanlış girdiğiniz değerleri düzeltmek için;                                                                                           *")
                                    print("*    - Doktor Takviminden Randevu Çıkarma Paneli' nden  randevuyu silip tekrar buradan ekleyebilirsiniz.                                 *")
                                    print("*    - Doktor Takvimini Düzenleme Paneli' nden yanlış girdiğiniz randevuyu seçip düzeltebilirsiniz.                                      *")
                                    print("******************************************************************************************************************************************")
                                    print()
                                    randevu_zamani = input("Eklenecek zamanı giriniz: ")
                                    print("-------------------------------------")
                                    
                                    doktor.randevuEkle(int(dr_indeks),int(zaman_indeks),randevu_zamani)

                                    self.kayan_noktalar("İşleminiz gerçekleştiriliyor","Randevu Eklendi.")
                                    
                                    dongu = False
                                    break
                                        
                               

                            if not dongu:
                                break

                            print("Lütfen doğru bir değer girin !!!\n")




                    if secim_1 == "2":                                              # -- Doktor takviminden randevu çıkarma --
                        
                        while True:
                            print()
                            print("***************************************************")
                            print("*    Doktor Takviminden Randevu Çıkarma Paneli    *")
                            print("***************************************************")
                            print()

                            i, dr_indeks = self.doktorlariGoster()
                            if i == 0:
                                dongu = False
                                break

                            for j in range(1,i+1):                                   # dr_indeks degeri yanlis secilmemesi icin kontrol
                                
                                if int(dr_indeks) == j:
                                    
                                    while True:
                                        i = self.randevuGoster(int(dr_indeks))

                                        zaman_indeks = str(int(input("Çıkartmak istediğiniz randevu: ")) + 2)                     # dogru indeksi bulmak icin -1 yapmaklıyız ama -
                                                                                                            # zamanlar 3. indeksten basliyor (3-1=2) bu yüzden +2 ekle.
                                        
                                        if zaman_indeks == "2":                                                 # aslinda burada 0' a basti 
                                            exit()

                                        doktor = D(self.doktorlarData[(int(dr_indeks))][1],self.doktorlarData[int(dr_indeks)][2],self.doktorlarData)
                                        for j in range(3, i+3):                                               # Yanlis deger secilmemesi icin kontrol
                                            if zaman_indeks == str(j):
                                                doktor.randevuSil(int(dr_indeks),int(zaman_indeks))
                                                self.kayan_noktalar("İşleminiz gerçekleştiriliyor","Randevu Silindi.")
                                                dongu = False
                                                break
                                        
                                        if not dongu:    
                                            break
                                        print("\nLütfen doğru bir değer girin !!!\n")
                                    
                                    break

                            if not dongu:
                                break

                            print("Lütfen doğru bir değer girin !!!\n")





                    if secim_1 == "3":                                              # -- Doktor takvimini düzenleme --
                        
                        while True:
                            print()
                            print("***************************************************")
                            print("*       Doktor Takvimini Düzenleme Paneli         *")
                            print("***************************************************")
                            print()

                            i, dr_indeks = self.doktorlariGoster()
                            
                            if i == 0:
                                dongu = False
                                break

                            for j in range(1,i+1):                                   # dr_indeks degeri yanlis secilmemesi icin kontrol
                                
                                if int(dr_indeks) == j:
                                    
                                    while True:
                                        i = self.randevuGoster(int(dr_indeks))

                                        zaman_indeks = str(int(input("Düzenlemek istediğiniz randevu: ")) + 2 )    # dogru indeksi bulmak icin -1 yapmaklıyız ama -
                                                                                                                        # zamanlar 3. indeksten basliyor (3-1=2) bu yüzden +2 ekle.
                                        
                                        if zaman_indeks == "2":                                                           # aslinda burada 0' a basti 
                                            exit()

                                        print()
                                        print("******************************************************************************************************************************************")
                                        print("*                                                         DİKKAT!!! :                                                                    *")
                                        print("*----------------------------------------------------------------------------------------------------------------------------------------*")
                                        print("*- Gireceğiniz değeri yukarıdaki düzen doğrultusunda girmeye özen gösteriniz !                                                           *")
                                        print("*- Yanlış girdiğiniz değerleri düzeltmek için;                                                                                           *")
                                        print("*    - Buradan yanlış girdiğiniz randevuyu seçip düzeltebilirsiniz.                                                                      *")
                                        print("*    - Doktor Takviminden Randevu Çıkarma Paneli' nden  randevuyu silip, Doktor Takvimine Randevu Ekleme Panel'nden ekleyebilirsiniz.    *")
                                        print("******************************************************************************************************************************************")
                                        print()
                                        randevu_zamani = input("Yeni randevu zamanı: ")
                                        print("--------------------------------")

                                        if zaman_indeks == "2":
                                            exit()

                                        doktor = D(self.doktorlarData[int(dr_indeks)][1],self.doktorlarData[int(dr_indeks)][2],self.doktorlarData)
                                        for j in range(3, i+3):                                               # Yanlis deger secilmemesi icin kontrol
                                            if zaman_indeks == str(j):
                                                doktor.randevuDuzenle(int(dr_indeks), int(zaman_indeks), randevu_zamani)
                                                self.kayan_noktalar("İşleminiz gerçekleştiriliyor","Randevu Düzenlendi.")
                                                dongu = False
                                                break
                                        
                                        if not dongu:    
                                            break
                                        print("\nLütfen doğru bir değer girin !!!\n")
                                    
                                    break

                            if not dongu:
                                break

                            print("Lütfen doğru bir değer girin !!!\n")




                    if secim_1 == "00":                                              # -- Personel paneline geri dön --
                        break

                    if secim_1 == "0":                                              # -- Çıkış Yap --
                        exit()
                    
                    else:
                        if dongu:    
                            print("Lütfen doğru bir değer girin !!!\n")





            if secim == "2":                                                         # -- Randevuları onaylama ya da iptal etme --
                
                dongu = True
                while dongu:
                    print()
                    print("***************************************************")
                    print("*  Randevuları Onaylama ya da İptal Etme Paneli   *")
                    print("***************************************************")
                    print()
                    print("***************************************************")
                    print("* 1- Randevu Onaylama                             *")
                    print("* 2- Randevu iptal etme                           *")
                    print("* 00- Geri Dön                                    *")
                    print("* 0- Çıkış Yap                                    *")
                    print("***************************************************")
                    print()
                    secim_2 = input("Lütfen yapmak istediğiniz işlemi seçin: ")
                    print("-----------------------------------------")
                    
                    time.sleep(0.5)
                    os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle

                    if secim_2 == "1":
                        pass
                    if secim_2 == "2":
                        pass
                    if secim_2 == "00":
                        break
                    if secim_2 == "0":
                        exit()
                    else:
                        print("\nLütfen doğru bir değer girin !!!\n")    

            if secim == "3":                                                         # -- Hasta bilgilerine erişim --
                
                dongu = True
                while dongu:
                    print()
                    print("***************************************************")
                    print("*         Hasta Bilgilerine Erişim Paneli         *")
                    print("***************************************************")
                    print()
                    print("***************************************************")
                    print("* 1- Hastanın randevularını görünüleme            *")
                    print("* 2- Randevular listesini görüntüleme           *")
                    print("* 00- Geri Dön                                    *")
                    print("* 0- Çıkış Yap                                    *")
                    print("***************************************************")
                    print()
                    secim_3 = input("Lütfen yapmak istediğiniz işlemi seçin: ")
                    print("-----------------------------------------")
                    
                    time.sleep(0.5)
                    os.system('cls')                                                # ekranda 0.5sn gozuk sonra terminali temizle
                    
                    if secim_3 == "1":                                                          # -- Hastanın randevularını görünüleme --
                        
                        print()
                        print("***************************************************")
                        print("*     Hastanın Randevularını Görünüleme Paneli    *")
                        print("***************************************************")
                        print()
                        while True:
                            tc = input("\nHastanın TC kimlik numarısını girin: ")
                            print("------------------------------------------------")
                            print()

                            if len(str(tc)) == 11:

                                print("    HastaTC    /   Dr ID  /     Doktorun Adı         /  Randevu Tarihi  /   Randevu Saati  /  Durum")
                                print("----------------------------------------------------------------------------------------------------")
                                sira = 0
                                for hasta in self.randevularData[1:]:

                                    if len(hasta) > 1: 
                                        if hasta[0] == tc:
                                            sira +=1
                                            print(f"{sira}- {hasta[0]:<11}  /  {hasta[1]:<5}  /  {hasta[2]:<20}  /  {hasta[3]:<14}  /  {hasta[4]:<15}  /  {hasta[5]}")
                               
                                if sira == 0:
                                    print()
                                    print("***************************************************")
                                    print("* Aradığınız hastanın randevuları bulunmamaktadır *")
                                    print("***************************************************")
                                    print()
                                print("----------------")
                                print("00- Geri Dön ")
                                print("0- Çıkış Yap")
                                
                                while True:
                                    
                                    x = input("\n Seçiminiz: ")
                                    if x == "00":
                                        dongu = False
                                        break
                                    elif x == "0":
                                        exit()

                                    print("\nLütfen doğru bir değer girin !!!")   

                            if not dongu:
                                break          


                            else:
                                print("\nEksik yada yanlış tuşladınız. Tekrar Deneyiniz.")
                    
                    if not dongu:
                        break 
                    

                    if secim_3 == "2":                                                          # -- Randevularım listesini görüntüleme --
                        
                        print()
                        print("***************************************************")
                        print("*    Randevular Listesini Görüntüleme Paneli    *")
                        print("***************************************************")
                        print()
                        while True:

                            print("    HastaTC    /   Dr ID  /     Doktorun Adı         /  Randevu Tarihi  /   Randevu Saati  /  Durum")
                            print("----------------------------------------------------------------------------------------------------")
                            sira = 0
                            for hasta in self.randevularData[1:]:
                                
                                if len(hasta) > 1: 
                                        sira +=1
                                        print(f"{sira}- {hasta[0]:<11}  /  {hasta[1]:<5}  /  {hasta[2]:<20}  /  {hasta[3]:<14}  /  {hasta[4]:<15}  /  {hasta[5]}")
                            
                            if sira == 0:
                                print()
                                print("***************************************************")
                                print("*       Randevusu olan hasta bulunmamaktadır      *")
                                print("***************************************************")
                                print()
                            print("---------------")
                            print("00- Geri dön")
                            print("0- Çıkış Yap")
                            
                            while True:
                                
                                x = input("\n Seçiminiz: ")
                                if x == "00":
                                    dongu = False
                                    break
                                elif x == "0":
                                    exit()

                                print("\nLütfen doğru bir değer girin !!!")   

                            if not dongu:
                                break          


                            else:
                                print("\nEksik yada yanlış tuşladınız. Tekrar Deneyiniz.")
                    




                    if secim_3 == "00":
                        break
                    if secim_3 == "0":
                        exit()
                    else:
                        print("\nLütfen doğru bir değer girin !!!\n")   

            if secim == "00":                                                         # -- Ana Safya Don --       
                break
            if secim == "0":                                                         # -- Cikis yap --
                exit()
            else:                                                                  # -- Yanlis karakter secildi --
                if dongu:
                    print("\nLütfen doğru bir değer girin !!!")   



    def doktorlariGoster(self):                                                  # Doktorları gosterir
        
        print("\n     Doktorun Adı         /       Branşı")
        print("--------------------------------------------")
        
        i = 0
        dizi = []
        for dr in self.doktorlarData[1:]:               
            
            i += 1
            dizi.append(str(i))
            if len(dr) > 1:                               # bos satir varsa atla
                print(f"{i}- {dr[1]:<20}  /  {dr[2]}   ")
        
        print("\n--------------")
        print("00- Geri Dön ")
        print("0- Çıkış Yap")

        a = True
        while True:           
            dr_indeks = input("Randevu eklenecek doktoru seçin: ")
            print("---------------------------------")

            if dr_indeks in dizi:
                break
            elif dr_indeks == "00":
                a = False
                break      

            elif dr_indeks == "0":
                exit()
            
            print("\nLütfen doğru bir değer girin !!!")

        if not a:                                    
            return 0,0                                        # Hastanede doktor olmazsa burasi yuzunden hata verir!!
        
        return i, dr_indeks
        

                                                                    
            
        
            


    def randevuGoster(self,dr_indeks):                                         # Secilen doktorun randevularini gosterir

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
            print()
            print("***************************************************")
            print("*          Görüntülenecek randevu yok             *")
            print("***************************************************")
            print()
        print("---------------")
        print("0- Çıkış Yap")
        
        return i



    @staticmethod
    def kullanici_dogrula(ad, sifre,personelData):
        
        for personel in personelData[1:]:
            
            if (personel[0] == ad and personel[1] == sifre):
                return True,personel
        
        return False , None

