"""
def intervalo(x,num):
    if num in x:
        print()
        print("Sim!!!. O número", num,"está no intervalo de",min,"-",max)
    else:
        print()
        print(30 * '-')
        print("O número desejado não está no intervalo determinado!")

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Número inválido.")

try:

    min = input_int("Informe o primeiro número desse intervalo: ")
    max = input_int("Informe o ultimo número desse intervalo: ")
    num = input_int("Informe o número que deseja saber se está no intervalo: ")

    l = list(range(min, max+1))
    intervalo(l,num)
except:
    print(30*'-')
    print("Digite um número interio!!")
"""

#Tratamento de Exceções Multiplas
"""
def erro(x):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


#TypeError
erro("int+int")
#NameError
erro("a")
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")

erro(10*2)
print(50 * '-')
print("A aplicação foi finalizada!!")
"""
#Variação de uso
"""
def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ou Name Erro ocorreu!")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


#TypeError
erro("int+int")
#NameError
erro("a")
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")

erro(10*2)
print(50 * '-')
print("A aplicação foi finalizada!!")
"""
#Capturando a instância do erro
"""
def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e)) #instâcia da exceção
        print(type(e.args)) #argumentos as mensagens
        print(e) # __str__ mensagem
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError, NameError) as e:
        print(type(e)) #instâcia da exceção
        print(type(e.args)) #argumentos as mensagens
        print(e) # __str__ mensagem

#TypeError
erro("int+int")
#NameError
erro("a")
#ValueError
#erro("int('a')")
#ZeroDivisionError
#erro("5/0")

#erro(10*2)
print(50 * '-')
print("A aplicação foi finalizada!!")
"""
#Bloco Else na exceção (quando não há exceção PULA pro bloco else)
"""
def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print(type(e)) #instâcia da exceção
    except ZeroDivisionError as e:
        print(type(e))
    except (TypeError, NameError) as e:
        print(type(e)) #instâcia da exceção
    else:
        print("Nenhuma EXCEÇÂO ocorreu")

#TypeError
erro("int+int")
#NameError
erro("a")
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")

print(30 * '-')
erro("10+2")

print("A aplicação foi finalizada!!")
"""
#Bloco Finally (SEMPRE será executado)
"""
def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print(type(e)) #instâcia da exceção
    except ZeroDivisionError as e:
        print(type(e)) #instâcia da exceção
    except (TypeError, NameError) as e:
        print(type(e)) #instâcia da exceção
    else:
        print("Nenhuma EXCEÇÂO ocorreu")
    finally:
        print()
        print("SEMPRE será executado")

#TypeError
erro("int+int")
#NameError
erro("a")
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")

print(30 * '-')
erro("10+2")

print("A aplicação foi finalizada!!")
"""