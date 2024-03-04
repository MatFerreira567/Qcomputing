#Questão 1
from math import sqrt
from numpy import conj
a = 1
b = 2
c = 1
delta = b**2 -4*a*c
x1 = (-b + delta)/2
x2 = x1
try:
    raiz = sqrt(x1)
except ValueError:
    print("A equação não possui soluções reais")

#Questão 2
power = input("Insira o expoente")
if (power%4 == 0):
    reposta = 1
elif (power%4 == 1):
    reposta = complex(0,1)
elif (power%4 == 2):
    reposta = -1
elif (power%4 == 3):
    reposta = complex(0,-1)
print(reposta)

#Questao 3
c1 = complex(3,-1)
c2 = complex(1,4)
a = c1 + c2
b = c1*c2
print(a)
print(b)

#Questao 4
a = complex(-1,1)
valor = a**2 + 2*a + 2 
print(valor)

#Questao 5
c1 = complex(input("Insira o primeiro numero"))
c2 = complex(input("Insira o segundo numero"))
c3 = complex(input("Insira o terceiro numero"))

#Letra a
valor1 = c1 + c2
valor2 = c2 + c1
print(valor1,valor2)

valor1 = c1*c2
valor2 = c2*c1
print(valor1,valor2)

#letra b
valor1 = (c1+c2)+c3
valor2 = c1+(c2+c3)
print(valor1,valor2)
valor1 = (c1*c2)*c3 
valor2 = c1*(c2*c3)
print(valor1,valor2)

#letra c
valor1 = c1*(c2+c3)
valor2 = (c1*c2)+(c1*c3)
print(valor1,valor2)

#Questao 6
#letra a
valor1 = abs(c1)*abs(c2)
valor2 = abs(c1*c2)
print(valor1,valor2)

#letra b
valor1 = abs(c1+c2)
valor2 = abs(c1)+abs(c2)
print(f"{valor1} <= {valor2}")

#Questão 7
#letra a
valor1 = conj(c1) + conj(c2)
valor2 = conj(c1+c2)
print(f"{valor1}, {valor2}")

#letra b
valor1 = conj(c1)*conj(c2)
valor2 = conj(c1*c2)
print(f"{valor1}, {valor2}")


