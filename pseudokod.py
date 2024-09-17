#iki sayının toplamı
# 1. Başla
# 2. İlk sayıyı kullanıcıdan al
deger1 = int(input("İlk sayıyı girin: "))

# 3. İkinci sayıyı kullanıcıdan al
deger2 = int(input("İkinci sayıyı girin: "))

# 4. deger1 ve deger2'yi topla
sonuc = deger1 + deger2

# 5. Sonucu ekrana yazdır
print("Toplam:", sonuc)

# 6. Bitir

#1'den 100'e kadar olan sayıları toplama
# 1. Başla
# 2. toplam değişkenini başlat
toplam = 0

# 3. 1'den 100'e kadar olan sayıları döngüye al
for sayi in range(1, 101):
    toplam += sayi  # toplam = toplam + sayi

# 4. Toplamı ekrana yazdır
print("1'den 100'e kadar olan sayıların toplamı:", toplam)

# 5. Bitir

#asal sayının kontrolü
import math

# 1. Başla
# 2. Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# 3. Sayı 1 veya daha küçükse asal değildir
if sayi <= 1:
    print(sayi, "asal değil")
else:
    # 4. 2'den sayının kareköküne kadar bir döngü
    asal = True
    for i in range(2, int(math.sqrt(sayi)) + 1):
        if sayi % i == 0:  # Eğer tam bölünürse
            asal = False
            break

    # 5. Sonuç
    if asal:
        print(sayi, "asal bir sayıdır.")
    else:
        print(sayi, "asal değil.")

# 7. Bitir

#dizideki kotrol eden sayıların kontrolü 
# 1. Başla
# 2. Bir dizi al
dizi = input("Bir dizi elemanlarını aralarında boşluk olacak şekilde girin: ").split()

# 3. Boş bir kontrol listesi oluştur
kontrol_listesi = []

# 4. Her bir eleman için döngü başlat
tekrar_var_mi = False
for eleman in dizi:
    if eleman in kontrol_listesi:  # Eğer eleman daha önce kontrol listesinde varsa
        print("Tekrar ediyor:", eleman)
        tekrar_var_mi = True
        break
    else:
        kontrol_listesi.append(eleman)

# 5. Eğer döngü bittiyse
if not tekrar_var_mi:
    print("Tekrar etmiyor.")

# 6. Bitir
