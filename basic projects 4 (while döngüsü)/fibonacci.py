# girlen "n" sayısında göre, n.ci fibonacci sayısını bulan while döngüsü

sayi=int(input("kaçıncı fibonacci sayısını istiyorsunuz: "))

# başlanıgç değerleri
a=0
b=1
i=2

while i<=sayi:
    if sayi==0:
        b=0
    t=b
    b=a+b
    a=t
    i=i+1
print(b)