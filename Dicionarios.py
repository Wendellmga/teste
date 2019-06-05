#Dicionarios
"""
d1 = {}
d1['aaa'] = 1000
print(d1)
print()
d2 = dict()
d2['bbb'] = 2000
d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)
print()
d2 = {1.1:"teste", 2.2:"teste2", 3:"teste3"}
print(d2)
print()
print(d2[1.1])
print(d2[3])
"""
#Funcoes do dicionario (.keys()/.values()/.get()
"""
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
    }
print(tel)
print(len(tel))
del(tel[36458899])
print(tel)
print()
print(tel.keys())
print(tel.values())
print()
print(tel[30301122])
print(tel.get(30301122))
"""
#.popitem()
"""
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
    }
print(tel)
tel.popitem()
print(tel)
tel.popitem()
print(tel)
tel.popitem()
print(tel)
tel.popitem()
print(tel)
"""
tel = {
    30301122: "Pericles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
    }
print(30301122 in tel)
print(30301120 in tel)
print()
tel2 = {99999999: "teste1", 55551111: "teste2"}
tel.update(tel2)
print(tel)
print(len(tel))
print()
t = (10,10,10)
tel[t] = "eXcript"
print(tel)


