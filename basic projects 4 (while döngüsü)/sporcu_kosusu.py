# Bir sporcu birinci gün "x" km koştu, daha sonra her gün bir önceki güne göre %10 artırdı. Koşucu hangi gün en az "y" km koşmuş olur.
# programa "x" ve "y" değerleri giriliyor ve program gün sayısını azıyor.

x = int(input("ilk gün kaç km koşuldu: "))
y = int(input("En aç koşulan km ( gün hesaplamak için ) : "))

gun=1

while x<y:
        x=x+(x*0.1)
        gun+=1
print(gun)