# 1 ile 10 arasında bilgisayasrın rastgele tuttuğu sayıyı tahmin etmeye çalışcağımız bir oyun programı yazalım.

import random

sayi=random.randint(1,10)

sayac=0

while True:
    tahmin=int(input("tahmininiz: "))
    if (1<=tahmin)and(tahmin<=10):
        if tahmin<sayi:
            print("Daha büyük sayı giriniz.")
        elif tahmin>sayi:
            print("Daha küçük sayı giriniz.")
        else:
            print("doğru tahmin")
    elif tahmin==0:
        break
    else:
        print("hatalı giriş!")
    sayac+=1
print(sayac,"defada bildiniz.")
        

