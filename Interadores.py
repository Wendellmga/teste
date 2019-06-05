#While
"""
x = 1
print("While")
while(x<=10):
    print(x)
    x+=1
"""
#while/else
"""
x = 1
print("While")
while(x<=10):
    print(x)
    x+=1
else:
    print("else")
print("fim")
"""
#for
"""
for c in "python":
    print(c)
"""
#range
"""
c = list(range(0,10,2))
print(c)
print()
s = list(range(0,50,2))
print(s)
print()
x = list(range(10))
print(x)
print()
v = list(range(0,100,3))
print(v)
print()
t = list(range(100,0,-3))
print(t)
print()
k = list(range(-100,0,3))
print(k)
"""
#for range
"""
for i in range(0,10,2):
	print(i)
print()
for x in range(-10, 0, 1):
    print(x)
print()
"""
#break
"""
print("Antes de entrar no laço")
print()
for item in range(10):
    print(item)
    if(item==6):
        print("A condição pre estabelecide retornou verdadeira.")
        break
print()
print("Depois de ter entrando no laço")
"""
#continue
"""
print()
print("Inicio")
i = 0
while(i<10):
    i += 1
    if(i%2==0):
        continue
    if(i>8):
        break
    print(i)
else:
    print("else")
print("Fim")
print()
"""