# girilen sayının bölenlerini bulna while döngüsü
sayi=int(input("sayı giriniz: "))
bolum=2

while bolum <= sayi:
    if sayi%bolum==0:
        print(bolum)
        sayi//=bolum
    else:
        bolum+=1
