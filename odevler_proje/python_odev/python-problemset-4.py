liste = []
yeni = []
boyut = int(input("Kac adet sayi girilecek => "))
for i in range(boyut):
    sayi = int(input("Bir sayi giriniz => "))
    if sayi % 2 == 0:
        liste.append(sayi)
    elif sayi % 2 == 1:
        liste.append(sayi)
        yeni.append(sayi)
print("Listedeki En Büyük Tek Sayı: ", max(yeni))