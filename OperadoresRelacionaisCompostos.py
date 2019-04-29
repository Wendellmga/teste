#ex1
"""
idade = int(input("Informe a sua idade: "))
print()
if (idade<=0):
    print("Sua idade está incorreta!")
else:
    if(idade>150):
        print("A sua idade ta maior que a de japones, not possible!!!!")
    else:
        if(idade>=18) and (idade<=120):
            print("Parabens, voce é de maior")
        elif(idade < 18):
                print("Voce precisa ter mais de 18 anos!!!")
"""
#Ex2
num1 = int(input("Digite um número: "))

if(num1> 10):
    #print("O valor é maior do que 10!")
    if(num1<=15):
        print("O valor é maior que 10, mas, menor do que 15.")
    else:
        if(num1<=50):
            print("O valor maior do que 10, mas, menor do que 50")
        else:
            print("O valor é maior que 50")
else:
    if(num1>5):
        print("O número é menor do que 10, mas, maior que 5!")
        if(num1==7):
            print("O número é igual a 7.")
    else:
        print("O valor é menor do que 5.")