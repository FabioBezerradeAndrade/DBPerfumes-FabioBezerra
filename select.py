import sqlite3

def titulo(n,s):
    print("=" * n)
    print(f"{s}" .center(n))
    print("=" * n)

path = r"C:\SQLite\aulas"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

#Perfumes  + Marcas
cursor.execute("SELECT * FROM Perfumes AS P JOIN Marcas AS M ON P.ID = M.ID")
tabela = cursor.fetchall()
titulo(50, "Perfumes X Marcas")
print("ID". ljust(5)+"Nome".ljust(15)+"Quantidade".ljust(15)+"Marcas".ljust(15))
for linha in tabela:
    #print(tabela)
    print(str(linha[0]).ljust(5), end="")
    print(str(linha[1]).ljust(15), end="")
    print(str(linha[2]).ljust(15), end="")
    print(str(linha[7]).ljust(15),  end="")
    print()

#Perfumes + Volumes
cursor.execute("SELECT * FROM Perfumes AS P JOIN Volumes AS V ON P.ID = V.ID")
tabela = cursor.fetchall()
titulo(50, "Perfumes X Volumes")
print("ID". ljust(5)+"Nome".ljust(15)+"Quantidade".ljust(15)+"Volumes".ljust(15))
for linha in tabela:
    #print(tabela)
    print(str(linha[0]).ljust(5), end="")
    print(str(linha[1]).ljust(15), end="")
    print(str(linha[2]).ljust(15), end="")
    print(str(linha[7]).ljust(15),  end="")
    print()

