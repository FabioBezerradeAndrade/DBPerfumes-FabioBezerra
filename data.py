import sqlite3

path = r"C:\SQLite\aulas"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()

#Perfumes
cursor.execute("INSERT INTO Perfumes VALUES(1, 'Nº5', 10, 1, 1, 1)")
cursor.execute("INSERT INTO Perfumes VALUES(2, 'flower', 10, 1, 2, 1)")
cursor.execute("INSERT INTO Perfumes VALUES(3, 'nina ricci', 5, 1, 3, 2)")

#Marcas
cursor.execute("INSERT INTO Marcas VALUES(1, 'Channel')")
cursor.execute("INSERT INTO Marcas VALUES(2, 'kenzo')")
cursor.execute("INSERT INTO Marcas VALUES(3, 'nina ricci')")

#Fixacoes
cursor.execute("INSERT INTO Fixacoes VALUES(1, 'Parfum')")
cursor.execute("INSERT INTO Fixacoes VALUES(2, 'Toilette')")
cursor.execute("INSERT INTO Fixacoes VALUES(3, 'Fraiche')")
cursor.execute("INSERT INTO Fixacoes VALUES(4, 'Cologne')")

#Volumes
cursor.execute("INSERT INTO Volumes VALUES(1, 'Ml')")
cursor.execute("INSERT INTO Volumes VALUES(2, 'Oz')")

#Essencia_Perfume
cursor.execute("INSERT INTO Essencia_Perfume VALUES(1, 1)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES(1, 2)")

#Essencias
cursor.execute("INSERT INTO Essencias VALUES(1, 'Doce')")
cursor.execute("INSERT INTO Essencias VALUES(2, 'Citrico')")
cursor.execute("INSERT INTO Essencias VALUES(3, 'Amadeirado')")
banco.commit()
