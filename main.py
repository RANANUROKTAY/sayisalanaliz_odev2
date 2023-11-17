import math
print("Birinci iterasyon degeri=")
x=2
denklem=4*math.e**(-0.5*x)-x
turevi=-2*math.e**(-0.5*x)-1
print(x-(denklem/turevi))
print("İkinci iterasyon degeri=")
x=x-(denklem/turevi)
denklem=4*math.e**(-0.5*x)-x
turevi=-2*math.e**(-0.5*x)-1
print(x-(denklem/turevi))
print("Üçüncü iterasyon degeri=")
x=x-(denklem/turevi)
denklem=4*math.e**(-0.5*x)-x
turevi=-2*math.e**(-0.5*x)-1
print(x-(denklem/turevi))
print("Dördüncü iterasyon degeri=")
x=x-(denklem/turevi)
denklem=4*math.e**(-0.5*x)-x
turevi=-2*math.e**(-0.5*x)-1
print(x-(denklem/turevi))
