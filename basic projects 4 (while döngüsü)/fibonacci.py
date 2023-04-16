# girlen "n" sayısında göre, n.ci fibonacci sayısını bulan while döngüsü
# while loop that finds the nth fibonacci number according to the number "n" entered


sayi=int(input("kaçıncı fibonacci sayısını istiyorsunuz: "))

# initial values
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