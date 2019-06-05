# Primeira Função
"""
def minha_fuc():
    print("Fala, galera!!")
minha_fuc()
"""
# Parâmetros da Função
"""
def soma(x, y):
    total = x + y
    print("O total da sima de x + y é: ", total)

soma(10, 50)
"""
#Parâmetros Default
"""
def login(usuario="root",senha="123"):
    print("Usuário:",usuario)
    print("Senha:",senha)

login("root","1234")
"""
#Agumentos posicionais e Argumentos nomeados
"""
def dados_pessoais(nome, sobrenome, idade, sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome, sobrenome, idade, sexo))

#posicional
dados_pessoais("Wendel", "Correia", "21", "Masculino")
#nomeada
dados_pessoais(nome="Lais", sobrenome="Mirelli", idade="21", sexo="Feminino")
"""
#Retorno de valores (return)
"""
def soma(x,y):
    num = x * y
    return num
print(soma(10,5))
"""
#Retorno de multiplos valores
"""
def func():
    return 1, 2

a, b = func()
print(a, b)
"""
"""
num = int(input("Informe um numero: "))
def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado,cubo

q,c = potencia(num)

print(q, c)
"""
#Funcao Variádica
"""
def lista_de_argumentos(*lista):
    print(lista)

def lista_de_argumentos_assiciativos(**dicionario):
    print(dicionario)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos("um","dois","tres","quatro")
print()
lista_de_argumentos_assiciativos(a=1, b=2, c=3, d=4)
lista_de_argumentos_assiciativos(um=1, dois=2, tres=3, quatro=4)
print()
argumentos(1,2,3,4, um=1, dois=2, tres=3, quatro=4)
"""
#Desempacotamento
"""
def pessoa (nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

lista = ["eXcript", "Brasil", 20]
#pessoa(tupla[0], tupla[1], tupla[2])
pessoa(*lista)
print()

d = {"nome":"eXcript", "sobrenome":"Brasil", "idade": 20}
pessoa(**d)
"""
"""
lista = [11, 10, 12]
tupla = 11, 10, 12

def func(a, b, c):
    print(a)
    print(b)
    print(c)

lista.sort()
func(*lista)

print()

l = [*tupla]
l.sort()
func(*l)
print()

func(**dict(zip(("a","b","c"), lista)))
"""
#Funções aninhadas
"""
def func():
    print("func")

    def func_interna():
        print("func_interna")

    func_interna()

func()
"""
#Instrução NONLOCAL
"""
def func():
    var_local = 10
    def func_interna():
        nonlocal var_local
        var_local += 1
        print(var_local)

    func_interna()
func()

#exemplo com uma variavel global
x = 10
def funcX():
    global x
    return x
print(funcX())
"""
#Blocos sem código (pass)
"""
def ainda_nao_sei_oq_escrever():
    pass

ainda_nao_sei_oq_escrever()
"""
#Instrução Global
"""
num = 10
print(num)

def func():
    global num #tem que definir com global pra alterar a variavel global na função
    num = 50
    print(num)

func()

print(num)
"""


















