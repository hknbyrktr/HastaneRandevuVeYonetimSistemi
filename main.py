from proje.base_classes.base_class import BaseClass as BC
from proje.sub_classes.hasta import Hasta as H
from proje.sub_classes.personel import Personel as P

import os
import time

def hastaKayitMenu():
    time.sleep(0.5)
    os.system('cls')                                                                    # ekranda 0.5sn gozuk sonra terminali temizle
    print()
    print("********************************************************************")
    print("*                                                                  *")
    print("*                      HASTA KAYIT PANELİ                          *")
    print("*                                                                  *")
    print("********************************************************************")
    print()
    print("\nVerilen bilgileri doldurun;")
    print("---------------------------")
    print()
    tc = input("TC Kimlik no: ")
    print("---------------------------")
    ad = input("Adınız: ")
    print("---------------------------")
    soyad = input("Soyadınız: ")
    print("---------------------------")
    sifre = input("Şifreniz: ")
    print()

    hastaKaydet(tc, ad, soyad, sifre)
    BC.kayan_noktalar("Bilgileriniz kaydediliyor","Bilgileriniz Kaydedildi.")



def hastaKaydet( tc, ad, soyad, sifre):
    yeni_satir = f"\n{tc},{ad},{soyad},{sifre},"
    
    with open("./proje/data/hastalar.txt", 'a', encoding='utf-8', newline='') as dosya:
        dosya.write(yeni_satir) 

    yeni_veri = yeni_satir.split(",")                                                       # Satiri virgule gore bolerek liste formatina donustur
    hastalarData.append(yeni_veri)
  


def main():
       
    os.system('cls')                                                    # Terminali temizle

    if TF == False:                                       # dosyalar okunmaz ise islemlere devam etmemek icin
        print("**************************************************************")
        print("* Biryerlerde hata olmalı lütfen kodunuzu kontrol ediniz !!! *")
        print("**************************************************************")
        exit()
        


    while True:
        
        print("********************************************************************")
        print("*                                                                  *")
        print("*              HASTANE RANDEVU VE YÖNETİM SİSTEMİ                  *")
        print("*                                                                  *")
        print("********************************************************************")
        print()
        print()
        print("********************************************************************")
        print("*                                                                  *")
        print("*                    1- Hasta Girişi                               *")
        print("*                    2- Personel Girişi                            *")
        print("*                    3- Hasta Kayıt                                *")
        print("*                    0- Çıkış yap                                  *")
        print("*                                                                  *")
        print("********************************************************************")
        print()
        secim = input("Seçiminiz: ")
        print("------------")

        if secim == "1":                                                           # -- Hasta Girisi --

            loop = True
            while loop:
                print()
                tc = input("\nTC Kimlik No: ")
                print("-------------------------")
                sifre = input("Şifre: ")
                print()
                print()
                hastalarData = H.dosya_okuma() 
                TorF, hastaSatir = H.kullanici_dogrula(tc, sifre,hastalarData)     # bilgiler dogru girildimi, dogruysa hastanin bilgilerinin old satiri dondur

                if TorF:
                    tcNo, ad, soyad, sifre, tibbiGecmis = hastaSatir
                    loop = H(tcNo,ad,soyad,sifre,tibbiGecmis,doktorlarData,hastalarData,randevularData).hastaMenusu()
                    
                else:
                    print()
                    print("***********************************************************")
                    print("* TC Kimlik numaranızı veya şifrenizi yanlış girdiniz !!! *")
                    print("* Tekrar Deneyin...                                       *")
                    print("***********************************************************")


        elif secim == "2":                                                           # -- Personel Girisi --
            
            loop = True
            while loop:
                ad = input("\nAdınız: ")
                print("--------------")
                sifre = input("Şifre: ")
                print()
                print()

                TorF, personelSatir = P.kullanici_dogrula(ad, sifre,personelData)     # bilgiler dogru girildimi, dogruysa hastanin bilgilerinin old satiri dondur

                
                if TorF:
                    ad, sifre, gorev = personelSatir
                    loop = P(ad, sifre, gorev, doktorlarData,randevularData,personelData).personelMenusu()
                    
                else:
                    print()
                    print("**********************************************")
                    print("* Adınızı veya şifrenizi yanlış girdiniz !!! *")
                    print("* Tekrar Deneyin...                          *")
                    print("**********************************************")


        elif secim == "3":                                                           # -- Hasta Kayit --
            hastaKayitMenu()

        elif secim == "0":
            print("**************************")
            print("* Sistemden çıkılıyor... *")
            print("**************************")
            print()
            break
        else:
            print("*********************************")
            print("* Hatalı seçim, tekrar deneyin. *")
            print("*********************************")
            print()
            print()

    

TF, doktorlarData, hastalarData, personelData, randevularData = BC.dosya_okuma()

if __name__ == '__main__':
    
    main()



