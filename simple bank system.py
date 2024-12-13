class Kullanici:
    def __init__(self, ad, hesap_numarasi, bakiye):
        self.ad = ad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL başarıyla yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Lütfen geçerli bir miktar girin.")

    def para_cek(self, miktar):
        if miktar > 0 and miktar <= self.bakiye:
            self.bakiye -= miktar
            print(f"{miktar} TL başarıyla çekildi. Kalan bakiye: {self.bakiye} TL")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            print("Lütfen geçerli bir miktar girin.")

    def bakiye_sorgula(self):
        print(f"Hesap Bakiyesi: {self.bakiye} TL")


class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_olustur(self, ad, hesap_numarasi, baslangic_bakiyesi):
        if hesap_numarasi in self.kullanicilar:
            print("Bu hesap numarası zaten mevcut.")
        else:
            yeni_kullanici = Kullanici(ad, hesap_numarasi, baslangic_bakiyesi)
            self.kullanicilar[hesap_numarasi] = yeni_kullanici
            print(f"Hesap başarıyla oluşturuldu. Hoşgeldiniz, {ad}!")

    def kullanici_girisi(self, hesap_numarasi):
        if hesap_numarasi in self.kullanicilar:
            return self.kullanicilar[hesap_numarasi]
        else:
            print("Hesap bulunamadı.")
            return None

# Banka sistemi oluşturuluyor
banka = Banka()

# Örnek işlemler
banka.hesap_olustur("Beyza", "12345", 500)
banka.hesap_olustur("Enes", "67890", 1000)

# Enes giriş yapıyor
enes_hesap = banka.kullanici_girisi("12345")
if enes_hesap:
    enes_hesap.bakiye_sorgula()
    enes_hesap.para_yatir(200)
    enes_hesap.para_cek(100)
    enes_hesap.bakiye_sorgula()

# Beyza giriş yapıyor
beyza_hesap = banka.kullanici_girisi("67890")
if beyza_hesap:
  beyza_hesap.bakiye_sorgula()
  beyza_hesap.para_cek(500)
  beyza_hesap.bakiye_sorgula()