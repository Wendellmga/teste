#Quest 1
""""
print("Wendel")
"""
#Quest 2
"""
nome = input("Digite seu nome nome:")

#print("Digite o seu nome: ", nome)
print("O seu nome é: %s, volte sempre" %nome)
"""
#Quest 3
""""
nome  = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
print()
print("O seu nome é %s, e a sua idade é " %nome + str(idade))
"""
#Quest 4
""""
numero = input("Informe um numero: ")
print()
print(numero)
"""
#Quest 5
""""
numero = int(input("Informe um numero: "))
print()
print("O número digitado foi: %i" %numero)
"""
#Quest 6
""""
numero1 = float(input("Digite número 1: "))
numero2 = float(input("Digite número 2: "))
numero3 = float(input("Digite número 3: "))
soma = numero1 + numero2 + numero3
print()
print("A soma total é: ", soma)
"""
#Quest 7
"""
numero1 = float(input("Digite número 1:"))
numero2 = float(input("Digite número 2:"))
soma = numero1 + numero2
print()
print("A soma entre %.1f e %.1f é igual a: %.1f" %(numero1,numero2,soma))
#print("A soma entre", numero1, "e", numero2, "é igual: ",soma)
"""
#Quest 8
"""
nota1 = float(input("Informe nota da primeira prova: "))
nota2 = float(input("Informe nota da segunda prova: "))
nota3 = float(input("Informe nota da terceira prova: "))
nota4 = float(input("Informe nota da quartaa prova: "))
media = (nota1+nota2+nota3+nota4)/4
print()
print("A media é: %.1f" %media)
"""
#Quest 9
"""
medidaMetros = float(input("Informe sua medida em metros: "))
centimetros = 100 * medidaMetros
print()
print("A sua medida em centimetros é: %.2f" %centimetros)
"""
#Quest 10
"""
num = float(input("Informe o numero a ser convertido: "))
quadrado = num ** 2
cubo = num ** 3
print()
print("O quadrado de", num, "é:", quadrado, ", e o cubo é:", cubo)
"""
#Quest 11
"""
num_1 = int(input("Digite o numero 1:"))
num_2 = int(input("Digite o numero 2:"))
div = num_1/num_2
divInteiro = num_1 // num_2
print()
print("O decimal total é: ",div)
print("E o total inteiro é: ",divInteiro)
"""
#Quets12
"""
largura = float(input("Informe a largura do triangulo: "))
altura = float(input("Informe a altura do triangulo: "))
print("Sua altura esta em metros? ")
resposta = input("s/n?") 
print()
if(resposta == 'n'):
    larguraMetro = largura / 100
    alturaMetro = altura / 100
    area = (larguraMetro * alturaMetro) / 2
    print("A area total do triangulo possui", area, "metros quadrados")
else:
    area = (largura * altura) / 2
    print("A area total do triangulo possui", area, "metros quadrados")
"""
#Quest 13
"""
dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas (Max 24): "))
minutos = int(input("Informe a quantidade de minutos (Max 60): "))
segundos = int(input("Informe a quantidade de segundos(Max 60): "))

segundosDia = dias * 86400
segundosHora = horas * 3600
segundosMinuto = minutos * 60
totalSegundos = segundosDia + segundosHora + segundosMinuto + segundos
print()
print(dias, "dia(s), tem", segundosDia, "segundos;", horas, "hora(s), tem", segundosHora,"segundos;", minutos,"minutos tem,", segundosMinuto,",e", segundos," segundo(s)")
print("Total de segundos é: ",totalSegundos, "segundos.")
"""
#Quest 14
"""
valorCompra = float(input("Informe o valor da compra: "))
desconto = valorCompra * 0.1
print()
print("O valor total da compra é de: R$%.2f, mas, com o desconto de 10/c o valo CAIU para R$%.2f" %(valorCompra,desconto))
"""






