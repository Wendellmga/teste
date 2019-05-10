#Quest1
"""
print(list(range(1, 100, 1)))
"""
#Quest2
"""
x = 1
while(x > 0):
    intervalo1 = int(input("Digite o primeiro número: "))
    intervalo2 = int(input("Digite o ultimo número: "))
    if(intervalo1 != intervalo2):
        print(list(range(intervalo1, intervalo2 +1, 1)))
        break
    else:
        print()
        print("Digite números diferentes")
        print()
"""
#Quest3
"""
print(list(range(-10, 1, 1)))
"""
#Quest4
"""
print(list(range(2, 100, 2)))
"""
#Quest5
"""
num = 0
cont = 0
while(num <= 100):
    num += 1
    if(num%2==0):
        cont += 1
print(cont)
"""
"""
numPar = list(range(0, 100, 2))
print(len(numPar))
"""
#Quest6
"""
#num = 0
#while(num<=100):
#    num += 1
#primo = num/1 == num and num/num == num == True
#print(list(range(0,100,primo)))
"""
"""
for i in range(1,101,1):
    for div in range(i-1,0,-1):
        modul=i%div
        if modul==0 and div>1:
            break
        elif div==1:
            print(i)
"""
"""
num = list(range(100))
for n in num:
    cont_divisores = 0
    for divisor in range(1, n + 1):
        if (n % divisor == 0):
            cont_divisores += 1
    if (cont_divisores == 2):
        print(n)
"""
#QUest7
"""
print("Descubra os números primos entre um intervalo.")
i = int(input("Digite o primeiro número: "))
f = int(input("Digite o segundo número: "))
print()

while(f < i):
    print("Erro!, o primeiro número necessariamente precisa ser menor que o segundo.")
    print()
    i = int(input("Digite o primeiro número: "))
    f = int(input("Digite o segundo número: "))
else:
    num = list(range(i, f))
    for n in num:
        cont_divisores = 0
        for divisor in range(1, n + 1):
            if (n % divisor == 0):
                cont_divisores += 1
        if (cont_divisores == 2):
            print(n)
"""
#Quest8
"""
print("Estabeleca um intervalo de números. ")
print("===================================")
min = int(input("Entre com um valor inicial do intervalo: "))
lim = int(input("Entre com um valor maximo do intervalo: "))
lista = list(range(min, lim + 1, 1)) if min < lim else list(range(min, lim - 1, -1))
print()
print("Agora escolha 3 numeros a serem ignorados dentro desse intervalo")
print()
num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Terceiro numero: "))
print()
for n in lista:
    if (n != num1 and n != num2 and n != num3):
        print(n)
"""
#Quest9
"""
print("Estou em looping")
letra = input("Digite uma letra: ")
while(letra != "q"):
    if (letra != "q"):
        print("Estou em looping")
        letra = input("Digite uma letra: ")
    elif (letra == "q"):
        break
"""
"""
loop = True
while(loop):
    print("estou em looping")
    print("Entre com uma litra 'q' para sair")
    if(input() == "q"):
        break
    else:
        continue
"""







