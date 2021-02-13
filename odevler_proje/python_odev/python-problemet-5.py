class Okul:
    def __init__(self,bolum,sinif,ogrt_say,ogr_ad,ogr_num,ogr_ort):
        self.bolum=bolum
        self.sinif=sinif
        self.ogrt_say=ogrt_say
        self.ogr_ad=ogr_ad
        self.ogr_num=ogr_num
        self.ogr_ort=ogr_ort





    def bilgi_goster(self):
        print("*-"*20)
        print("Okulun bölümü:",self.bolum)
        print("Sınıf sayısı:",self.sinif)
        print("Ogretmen sayısı:",self.ogrt_say)
        print("Okulun Birincisi")
        print("Adi: ",self.ogr_ad)
        print("Numarası: ",self.ogr_num)
        print("Ortalaması: ",self.ogr_ort)



okul1 = Okul("sayisal", 4, 30,"Betül","190",87.2)
okul2 = Okul("sozel", 5, 40,"Ayse","200",88.4)
okul3 = Okul("dil", 5, 15,"Ahmet","210",67.4)

okul1.bilgi_goster()
okul2.bilgi_goster()
okul3.bilgi_goster()
