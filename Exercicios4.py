#Quest1
"""
def estudo():
    print()
    print("Estamos estudando as funções.")
    return 0

estudo()
"""
#Quest2
"""
def estudo(n):
    print()
    print("Função invocada com suceso. O valor passado pelo argumento x é: ",n)
    return 0

while True:
    try:
        x = int(input("Digite um número: "))
        print()
        estudo(x)
        break
    except:
        print()
        print("Digite apenas número inteiro.")
        print()
"""
#Quest3
"""
def soma(x, y):
    total = x + y
    print("A soma dos valores é: ",total)
    return 0

while True:
    try:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        soma(a,b)
        print()
        break
    except:
        print()
        break
"""
#Quest4
"""
def ordemMedia(a, b, c):
    lista = [a, b, c]
    #ordem = sorted(lista)
    lista.sort()
    print()
    print("A ordem é:")
    #print(ordem[0], ordem[1], ordem[2])
    print(lista)
    media = (a + b + c)/3
    print("A média é: ", media)
    return 0

while True:
    try:
        x = float(input("Digite o primeiro valor: "))
        y = float(input("Digite o segundo valor: "))
        z = float(input("Digite o terceiro valor: "))
        ordemMedia(x,y,z)
        print()
        break
    except:
        print()
        break
"""
#Quest5
"""
def dados(nome, idade):
    nome = input("Digite p seu nome: ")
    opcao = input("Deseja nos informar a sua idade? 's/n': ")
    if opcao == 's':
        idade = int(input("Informe a sua idade: "))
        #print("Seu nome:", nome,"Sua idade:", idade)
        print('''
        nome:{}
        idade:{} anos'''.format(nome,idade))
    elif opcao == 'n':
        print(nome)
dados('nome','idade')
"""
#Quest6
"""
def func1():
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))
    def func2(x,y):
        soma = x + y
        print("A soma dos números é: ",soma)
    return func2(x,y)
    #func2(x,y)
func1()
"""
#Quest7
"""
def Parametros(lista):
    for p in lista:
        print(p)

lista = []
while True:
    lista.append(input("Digite um parâmetro a ser inserido, ou digite 'sair' para sair do programa: "))
    if 'sair' in lista:
        lista.remove('sair')
        break
Parametros(lista)
"""
#Quest8
"""
dic = {}
z = 0
x = 0

def imprime(dicionario):
    print('Os parâmetros com suas respectivas chaves são: ')
    print('')
    for i in dicionario:
        print(str(i) + ':', dicionario[i] + ';')
    return 0

while (x != 'sair'):
    x = input("Digite um parâmetro, ou digite 'sair' para fechamento do programa: ")
    if (x == 'sair'):
        imprime(dic)
        break
    dic[z] = x
    z += 1
"""
#Quest9
"""
def func(a, b, c, d):
    print(a+b+c+d)

lista = 1,2,3,4

l = [*lista]

func(*lista)
"""
#Quest10
"""
def func10(*x):
    x = sorted(x)
    print(x[-1])


l = input("Escolha numeros(separados por espaços): ")
l = l.split(" ")

func10(*l)
"""
#Quest11
"""
def somaLista(*lista):
    y = 0
    for i in lista:
        y += int(i)
    print(lista)
    print(y)

x = []
while True:
    x.append(input("Insira um número na lista, ou digite 'sair' para fechar o programa: "))
    print()
    if 'sair' in x:
        x.remove('sair')
        break
somaLista(*x)
"""
#Quest12
"""
def multiplicaLista(*listamult):
    y = 1
    for i in listamult:
        y = y * int(i)
    print(listamult)
    print(y)

lista = []
while True:
    lista.append(input("Insira um número na lista, ou digite 'sair' para fechar o programa: "))
    if 'sair' in lista:
        lista.remove('sair')
        break
multiplicaLista(*lista)
"""
#Quest13
"""
def ivterte_lista(*lst):
    lista_inv = []
    for i in lst:
        lista_inv.append(i[::-1])
    print('-' * 30)
    print(lista_inv)

lista = []
while True:
    lista.append(str(input("Informe um valor p/ a lista: ")))
    sair = str(input("Deseja add mais um item a lista: [S/N] ")).strip()[0]
    if sair in "Nn":
        break
ivterte_lista(*lista)
"""
#Quest14
"""
def fatorial(num):
    if num <= 0:
        print(50*'-')
        print("Não é possível calcular!")
    else:
        y = 1
        while num != 0:
            y = y * num
            num -= 1
        print()
        print(y)

x = int(input("Digite um valor (inteiro) para ser calculado o fatorual: "))
fatorial(x)
"""
#Quest15
"""
def intervalo(x,num):
    if num in x:
        print()
        print("Sim!!!. O número", num,"está no intervalo de",min,"-",max)
    else:
        print()
        print(30 * '-')
        print("O número desejado não está no intervalo determinado!")

try:
    min = int(input("Informe o primeiro número desse intervalo: "))
    max = int(input("Informe o ultimo número desse intervalo: "))
    num = int(input("Informe o número que deseja saber se está no intervalo: "))

    l = list(range(min, max+1))
    intervalo(l,num)
except:
    print(30*'-')
    print("Digite um número interio!!")
"""
#Quest16
"""
def func16(x):
    y = 0
    z = 0
    for i in x:
        if i == " ":
            continue
        if i is ",":
            continue
        elif i is "!":
            continue
        elif i is ":":
            continue
        elif i is "@":
            continue
        elif i is "#":
            continue
        elif i is "%":
            continue
        elif i is "-":
            continue
        elif i is "/":
            continue
        elif i is "+":
            continue
        elif i is "$":
            continue
        elif i is ";":
            continue
        elif i is ".":
            continue
        elif i is "<":
            continue
        elif i is ">":
            continue
        elif i is "'":
            continue
        elif i is "=":
            continue
        elif i is "(":
            continue
        elif i is ")":
            continue
        if i.isupper() == True:
            y += 1
        if i.isupper() == False:
            z += 1

    print("A palavra tem:\n", y, "letras maiusculas e", z, "letras minusculas")

l = input("Escolha uma palavra ou frase: ")
func16(l)
"""
#Quest17
"""
def func17(*x):
    z = []
    for i in x:
        if i in z:
            continue
        z.append(i)
    print(z)


l = input("Escolha numeros(separados por espaços): ")
l = l.split(" ")
func17(*l)
"""
#Quest18
"""
def func17(*x):
    z = []
    for i in x:
        i = int(i)
        divisores = 0
        for divisor in range(1, i):
            if i % divisor == 0:
                divisores = divisores + 1
        if divisores > 1:
            continue
        if divisores == 1:
            z.append(i)
    print(z)

l = input("Escolha numeros(separados por espaços): ")
l = l.split(" ")
func17(*l)
"""
#Quest19
"""
def pares(*x):
    z = []
    for i in x:
        if int(i) % 2 == 0:
            z.append(int(i))
    print(z)

l = input("Escolha numeros(separados por espaços): ")
l = l.split(" ")
pares(*l)
"""
#Quest20
"""
def palindromo(l):
    l = l.replace(" ", "") #retira os espaços da string para que seja possível verificar se uma frase também é um palindromo
    if str(l) == str(l[::-1]):
        print()
        print(l,"é um palindromo.")

x = str(input("Digite a palavra ou frase: "))
palindromo(x)
"""
#Quest21
"""
def func1():
    def func2():
        return "Okay"
    print(func2())
func1()
"""










