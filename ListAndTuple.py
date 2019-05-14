#Listas
"""
lista = ["a","b","c","d"], ["a","e","i","o","u"], [12,15,651,15,51]
print(len(lista))
print(len(lista[0]))
print(lista[0][-1])
print()

listaa = list([0,1,2,3])
listaa.append(4)
print(listaa)
del(listaa[0])
print(listaa)
listaa += [5]
print(listaa)
listaa = [0] + listaa
print(listaa)
listaa += [6,7,8,9] #lista = lista + [6,7,8,9]
print(listaa)
"""
#Interação com listas
"""
lista_nums = [100,200,300,400,500,600,700]
for item in range(len(lista_nums)):
    lista_nums[item] += 1000
print(lista_nums)
"""
"""
lista_nums = [100,200,300,400,500,600,700]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)
"""
#Fatiar Listas/ list(start:len:step)
"""
lista = list("Python")
print(lista[2:])
print(lista[:2])
print(lista[::2])
print(lista[2::2])
print(lista[::-1])
"""
"""
lista = "Bem-vindo ao Curso de Python"
print(lista[10])
print(lista[:20])
print(lista[10:20])
print(lista[::2])
print(lista[::-1])
"""
#Incluir, Alterar e Excluir elementos
"""
l = ['bbb','ccc','ddd']
print(l)
l.append('eee')
print(l)
l.insert(0, 'aaa')
print(l)
l[1] = 'bbbb'
print(l)
#l.clear()
print(l)
l.pop()
print(l)
l.pop(0)
print(l)
l.pop(-1)
print()
l.insert(0, 'aaa')
l[1] = 'bbb'
l.insert(-1, 'eee')
print(l)
l.clear()
l = ['bbb','ccc','ddd', 'eee']
print(l)
del(l[2:4])
print(l)
l = ['aaa','bbb','ccc','ddd', 'eee']
del(l[::2])
print(l)
"""
#Ordenamento de listas
"""
lista = ['Claudio', 'Jose', 'Maria', 'Beltrano', 'Joao', 'Fulano', 'Ciclano']
lista.reverse()
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
"""
#Quantidade de Elementos
"""
lista = ['Claudio', 'Jose', 'Maria', 'Beltrano', 'Joao', 'Fulano', 'Ciclano']
print(len(lista))
print(lista[len(lista)-1])
lista.insert(5, 'Jose')
print(lista)
lista.append('Jose')
print(lista)
print(lista.count('Jose'))
print(lista.index('Maria'))
"""
#Operador In
# a = 10
# b = 25
# c = 66
# x = int(input("Digite um numero: "))
#
# if(x in [a,b,c]):
#     print("Esta contido.")
# else:
#     print("Nao esta contido")
#--------------------------------------------
cores = ["azul","amarelo","vermelho","branco"
    ,"amarela","vermelha","branca"]

while True:
    cor = input("Digite o nome de uma cor, ou"
                " entao, digite 0 para sair do programa: ")
    print()
    if(cor == "0"):
        break
    elif cor in cores:
        print("Essa cor esta contida!")
    else:
        print("Essa cor nao esta contida!")
    print()







