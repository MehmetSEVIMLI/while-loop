# Girilen "n" saısına kadar sayıların karelerini yazan programı yazınız.

sayi=int(input("istediğiniz sayıyı giriniz: "))
sayac=1

while sayac*sayac <=sayi:
    print(sayac*sayac,end=" ")
    sayac+=1
    