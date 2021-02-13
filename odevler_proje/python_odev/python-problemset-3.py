list = []
yeni = []
boyut = int(input("Kac adet sayi gireceksiniz? => "))
for i in range(boyut):
    sayi=int(input("Sayi giriniz => "))
    if sayi==0:
        yeni.append(sayi)
    else:
        list.append(sayi)
list2 = []
list2 = yeni+list
print(list2)