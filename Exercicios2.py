#Quest1
"""
num = int(input("Digite um numero: "))
print()
if (num > 0):
    print("O numero", num, "é positivo ")
else:
    if (num < 0):
        print("O numero", num, "è negativo")
if (num == 0):
    print("O número é 0.")
"""
#Quest2
"""
num = float(input("Digite um número: "))
print()
if (num%2 == 0):
    print("O número é par")
else:
    print("O número é ímpar")
"""
#Quest3
"""
num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um outro número: "))
print()
if(num_1 > num_2):
    print("O número", num_1, "é maior do que o número", num_2)
else:
    if(num_2 > num_1):
        print("O número", num_2, "é maior do que o número", num_1)
    elif (num_1 == num_2):
        print("Os dois números são iguais")
"""
#Quest4
"""
idade = int(input("Informe a sua idade: "))
print()
if(idade<18) and (idade > 0):
    print("Desculpe, você ainda está na menoridade.")
if(idade <= 0):
    print("Desculpe, sua idade está incorreta.")
else:
    if(idade >= 18) and (idade <= 120):
        print("Parabéns, você é de maior.")
    if(idade > 120):
        print("Descupe, a sua idade está incorreta.")
"""
#Quest5
"""
idade = int(input("Qual a sua idade: "))
idademae = int(input("Informe a idade da sua mãe: "))
print()
idadefinal = (idademae - idade)
anofinal = 2019 - idade
print("A sua mãe o teve com", idadefinal,"anos, no ano de", anofinal)
"""
#Quest6
"""
print('-'*50)
"""
#Quest7
"""
#é igual a quest2
"""
#Quest8
"""
num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite um outro número: "))
print()
if (num_1 > num_2):
    print("Maior:",num_1,"Menor: ",num_2)
else:
    print("Maior:",num_2,"Menor: ",num_1)
"""
#Quest9
"""
num = float(input("Informe um numero: "))
print()
if(num % 1 == 0):
    print("O número %.0f é inteiro."%num)
else:
    print("O numero digitado não é inteiro.")
"""
#Quest10 *
"""
algo = input("Digite algo: ")
print()
if(type(algo) == str):
    print("Você digitou uma string")
"""
#Quest11
"""
num = float(input("Digite um número: "))
print()
if(num % 1 == 0):
    print("Esse número não é um decimal")
else:
    print("Esse número é um decimal")
"""
#Quest12
"""
num = float(input("Digite um número: "))
print()
if(num % 1 == 0):
    print("Esse número é inteiro!")
else:
    print("Este número é decimal.")
"""
#Quest13
"""
num_1 = input("Digite um número: ")
num_2 = input("Digite outro número: ")
num_3 = input("Digite um outro número: ")
print()
if(num_1 >= num_2) and (num_1 >= num_3):
    print("O maior número é", num_1)
elif(num_2 >= num_3):
    print("O maior número é", num_2)
else:
    print("O maior número é", num_3)
"""
#Quest14
"""
num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite outro número: "))
num_3 = float(input("Digite um outro número: "))
print()
if(num_1 >= num_2) and (num_1 >= num_3):
    if(num_2 >= num_3):
        print("A crescente dos números é:", num_1,",",num_2,",",num_3)
    else:
        print("A crescente dos números é:", num_1, ",", num_3, ",", num_2)
if(num_2 >= num_1) and (num_2 >= num_3):
    if(num_3 >= num_1):
        print("A crescente dos números é:", num_2,",",num_3,",",num_1)
    else:
        print("A crescente dos números é:", num_2, ",", num_1, ",", num_3)
if(num_3 >= num_2) and (num_3 >= num_1):
    if(num_1 >= num_2):
        print("A crescente dos números é:", num_3,",",num_1,",",num_2)
    else:
        print("A crescente dos números é:", num_3, ",", num_2, ",", num_1)
"""
#Quest15
"""
carac = input("Digite um caractere: ")
print()
if (carac == "a" or carac == "e" or carac == "i" or carac == "o" or carac == "u"):
   print("O caractere digitado é uma vogal: ",carac)
elif (carac == "A" or carac == "E" or carac == "I" or carac == "O" or carac == "U"):
   print("O caractere digitado é uma vogal: ",carac)
else:
   print("Não é uma vogal")
"""
#Quest16
"""
ip = input("Digite o seu ip: ")
print()
if(ip >= '0') and (ip <= '127'):
    print("O ip", ip, "pertence a classe A")
elif(ip >= '128') and (ip <= '191'):
    print("O ip", ip, "pertence a classe B")
elif(ip >= '192') and (ip <= '223'):
    print("O ip", ip, "pertence a classe C")
elif(ip >= '224') and (ip <= '239'):
    print("O ip", ip, "pertence a classe D")
elif(ip >= '240'):
    print("O ip", ip, "pertence a classe E")
"""
#Quest17
"""
mes = int(input("Digite o número do mes desejado: "))
print()
if(mes == 1) or (mes == '01'):
    print("O mês escolhido é JANEIRO")
elif(mes == 2) or (mes == '02'):
    print("O mês escolhido é FEVEREIRO")
elif(mes == 3) or (mes == '03'):
    print("O mês escolhido é MARÇO")
elif(mes == 4) or (mes == '04'):
    print("O mês escolhido é ABRIL")
elif(mes == 5) or (mes == '05'):
    print("O mês escolhido é MAIO")
elif(mes == 6) or (mes == '06'):
    print("O mês escolhido é JUNHO")
elif(mes == 7) or (mes == '07'):
    print("O mês escolhido é JULHO")
elif(mes == 8) or (mes == '08'):
    print("O mês escolhido é AGOSTO")
elif(mes == 9) or (mes == '09'):
    print("O mês escolhido é SETEMBRO")
elif(mes == 10) or (mes == '10'):
    print("O mês escolhido é OUTUBRO")
elif(mes == 11) or (mes == '11'):
    print("O mês escolhido é NOVEMBRO")
elif(mes == 12) or (mes == '12'):
    print("O mês escolhido é DEZEMBRO")
"""
#Quest18
"""
data = input("Digite uma data no formato dd/mm/aaaa: ")
print()
if (len(data)==10):
    if(data[2] and data[5] == '/'):
        if(data[3] <= '1'):
            if(data[0] <= '3'):
                print("Data validada")
            else:
                print("O valor digitado não é valido para o formato de data")
"""


















