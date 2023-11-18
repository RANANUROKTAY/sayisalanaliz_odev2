#02220224004 - RANA NUR OKTAY - İKİNCİ ÖDEV
#İLK SORU
print("İLK SORU")
x_alt=2
x_ust=4
x_kok=(x_alt+x_ust)/2
numara=0
for i in  range(4):
        numara = numara + 1
        print("\n{}. iterasyon degeri=".format(numara))
        print("Alt kök=", x_alt)
        denklem_alt = x_alt ** 3 - 2 * x_alt ** 2 - 5
        print("Alt kökün degeri=", denklem_alt)
        print("Üst kök=", x_ust)
        denklem_ust = x_ust ** 3 - 2 * x_ust ** 2 - 5
        print("Üst kökün degeri=", denklem_ust)
        print("İkiye bölünmüş kök=", x_kok)
        denklem_boluk = x_kok ** 3 - 2 * x_kok ** 2 - 5
        print("İkiye bölünmüş kökün değeri=", denklem_boluk)
        print("Yeni kök değerleri=")
        if denklem_alt * denklem_boluk < 0:
                x_alt = x_alt
                x_ust = x_kok
                print(x_alt, "  ", x_ust)


        elif denklem_ust * denklem_boluk < 0:
                x_alt = x_kok
                x_ust = x_ust
                print(x_alt, "  ", x_ust)

        else:
                print("Denklem çözümü tıkandı. ")
        x_kok = (x_alt + x_ust) / 2

print("\n\n\n")

#İKİNCİ SORU
print("İKİNCİ SORU")
x_alt=1
x_ust=2
x_kok=(x_alt+x_ust)/2
numara=0
for i in  range(4):
        numara = numara + 1
        print("\n{}. iterasyon degeri=".format(numara))
        print("Alt kök=", x_alt)
        denklem_alt = x_alt ** 3 + 4 * x_alt ** 2 - 10
        print("Alt kökün degeri=", denklem_alt)
        print("Üst kök=", x_ust)
        denklem_ust = x_ust ** 3 + 4 * x_ust ** 2 - 10
        print("Üst kökün degeri=", denklem_ust)
        print("İkiye bölünmüş kök=", x_kok)
        denklem_boluk = x_kok ** 3 + 4 * x_kok ** 2 - 10
        print("İkiye bölünmüş kökün değeri=", denklem_boluk)
        print("Yeni kök değerleri=")
        if denklem_alt * denklem_boluk < 0:
                x_alt = x_alt
                x_ust = x_kok
                print(x_alt, "  ", x_ust)


        elif denklem_ust * denklem_boluk < 0:
                x_alt = x_kok
                x_ust = x_ust
                print(x_alt, "  ", x_ust)

        else:
                print("Denklem çözümü tıkandı. ")
        x_kok = (x_alt + x_ust) / 2

print("\n\n\n")

#ÜÇÜNCÜ SORU
print("ÜÇÜNCÜ SORU\n")
x=2
e=2.7182818284590452
numara=0
for i in  range(4):
        denklem = 4 * e ** (-0.5 * x) - x
        turevi = -2 * e ** (-0.5 * x) - 1
        numara=numara+1
        print("{}. iterasyon degeri=".format(numara))
        print(x - (denklem / turevi))
        x = x - (denklem / turevi)

print("\n\n")

#Kütüphane kullanılmış hali
print("Kütüphaneden alınan e değeri ile hesaplama:\n")
import math
x=2
numara=0
for i in  range(4):
        denklem = 4 * math.e ** (-0.5 * x) - x
        turevi = -2 * math.e ** (-0.5 * x) - 1
        numara=numara+1
        print("{}. iterasyon degeri=".format(numara))
        print(x - (denklem / turevi))
        x = x - (denklem / turevi)
