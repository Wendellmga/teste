#Sting
s1 = 'String com aspas simples'
#print(s1)
s2 = "String com aspas dupla"
#print(s2)
#print()
s3 = '''aaaaaaa
bbbbbbbb
cccccccc
ddddddddd
eeeeeeeeeeee'''
s4 = """aaaaaaa
bbbbbbbb
cccccccc
ddddddddd
eeeeeeeeeeee"""
#print(s3)
#print(s4)
#Fatiando String
"""
s = "Para o Python, toda String é uma lista imutável"
print(s)
print(s[0])
print(s[5:10])
print(s[5:20])
print(s[::-1])
print(s[::2])
"""
#Comparando Strings
"""
for c in range(123):
	print(str(c) + " - " + chr(c))
"""
#Propriedades das Strings
"""
s = "Lista de Caracteres"
print(len(s))
print(s.split(" "))
lista = s.split(" ")
print(lista[0] + " " + lista[2])
print(s.replace("de", "da"))
print(s.replace("de", ""))
print(s.replace(" ", ""))
print(id(s))
"""
#Interação de Strings
"""
s = 'Interando Strings'

for c in s:
    print(c)
"""
"""
s = 'Interando Strings'
indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice+=1
"""
"""
for k,v in enumerate('Interando Strings'):
    print(k, v)
"""































