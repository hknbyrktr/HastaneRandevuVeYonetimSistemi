"""
randevularData = []

try:
    with open("data/doktorlar.txt", "r", encoding="utf-8") as dosya:
        doktorlarData = [satir.split(",") for satir in dosya]
        print("okudu aq")
        

except FileNotFoundError:
    print("hani dosya aq")




doktorlarData[1].insert(8, "randevu_zamani")                     # doktorlarData guncelle
        
with open("data/doktorlar.txt", 'w', encoding='utf-8') as dosya:              # Dosyayi guncelle
    for doktor in doktorlarData:
        dosya.write(",".join(doktor) + "\n")                                          # Listeyi stringe dönüştürüp yaz
"""