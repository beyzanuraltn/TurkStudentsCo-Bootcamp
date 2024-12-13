class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar

class Sepet:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        for mevcut_urun in self.urunler:
            if mevcut_urun.ad == urun.ad:
                mevcut_urun.miktar += urun.miktar
                print(f"{urun.miktar} adet {urun.ad} sepete eklendi. (Toplam: {mevcut_urun.miktar})")
                return
        self.urunler.append(urun)
        print(f"{urun.miktar} adet {urun.ad} sepete eklendi.")

    def urun_cikar(self, urun_adi):
        for urun in self.urunler:
            if urun.ad == urun_adi:
                self.urunler.remove(urun)
                print(f"{urun.ad} sepetten çıkarıldı.")
                return
        print(f"{urun_adi} sepetinizde bulunamadı.")

    def sepeti_listele(self):
        if not self.urunler:
            print("Sepetiniz boş.")
            return
        print("Sepetinizdeki ürünler:")
        for urun in self.urunler:
            print(f"- {urun.ad}: {urun.miktar} adet, birim fiyatı: {urun.fiyat} TL")

    def toplam_tutar_hesapla(self):
        toplam_tutar = sum(urun.fiyat * urun.miktar for urun in self.urunler)
        print(f"Toplam Tutar: {toplam_tutar} TL")
        return toplam_tutar

# Örnek Kullanım
sepet = Sepet()

# Ürün ekleme
urun1 = Urun("Kurşun Kalem", 50, 2)
urun2 = Urun("A4 Kağıdı", 20, 3)
urun3 = Urun("Silgi", 5, 10)

sepet.urun_ekle(urun1)
sepet.urun_ekle(urun2)
sepet.urun_ekle(urun3)

# Sepeti listeleme
sepet.sepeti_listele()

# Ürün çıkarma
sepet.urun_cikar("A4 Kağıdı")

# Sepeti tekrar listeleme
sepet.sepeti_listele()

# Toplam tutarı hesaplama
sepet.toplam_tutar_hesapla()