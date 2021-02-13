dongu_kontrol = False
while not dongu_kontrol:
    kullanici_adi = input("kullanici adi giriniz:")
    uzanti = input("(@ sonraki ifade) uzanti adresi giriniz:")
    boyut = len(kullanici_adi)
    liste = list(kullanici_adi)
    boyut1 = len(uzanti)
    liste1 = list(uzanti)
    uzantikontrol = 0
    kontrol = 0
    kullanicikontrol = 0
    karakter = '-', '_'
    ana_karakter = '@'
    nokta = "."
    mail = kullanici_adi+uzanti
    if boyut >= 1 and boyut <= 12 and boyut1 >= 1 and boyut1 <= 60:
        for i in range(boyut):
            if liste[i].isupper():
                kontrol = 1
            elif liste[i].islower():
                kontrol = 1
        if kontrol == 0:
            kullanicikontrol = 1
        kontrol = 0

        for i in range(boyut):
            if liste[i] in karakter:
                kullanicikontrol = 0
                kontrol = 0
        kontrol = 0

        for i in range(boyut):
            if kullanici_adi.startswith(ana_karakter):
                kontrol = 1
                kullanicikontrol = 1
                break
            elif kullanici_adi.endswith(ana_karakter):
                kontrol = 0
                kullanicikontrol = 0
        if kontrol == 0:
            kullanicikontrol = 0
        kontrol = 0

        for i in range(boyut):
            if liste.count(ana_karakter) == 1:
                kontrol = 0
                kullanicikontrol = 0
            else:
                kullanicikontrol = 1
                kontrol = 1
        if kontrol == 0:
            kullanicikontrol = 0
        kontrol = 1

        for i in range(boyut1):
            if liste1[i] in nokta:
                if liste1.count(nokta) >= 1 and liste1.count(nokta) <= 2:
                    uzantikontrol = 0
                    kontrol = 0
                else:
                    uzantikontrol = 1
                    kontrol = 1
            if kontrol == 0:
                uzantikontrol = 0
        kontrol = 1

        for i in range(boyut1):
            if uzanti.startswith(nokta):
                kontrol = 1
                uzantikontrol = 1

            if uzanti.endswith(nokta):
                kontrol = 1
                uzantikontrol = 1
        if kontrol == 0:
            uzantikontrol = 0
        kontrol = 0


        if kullanicikontrol == 0 and uzantikontrol == 0:
            print('uzantı boyutu',liste1.count(nokta)+1)
            print(mail)
            print("BASARILI")
            dongu_kontrol = True
        else:
            print('uzantı boyutu', liste1.count(nokta) + 1)
            print(mail)
            print("BASARISIZ")

    else:
        print("GECERSIZ BOYUT.!!!")