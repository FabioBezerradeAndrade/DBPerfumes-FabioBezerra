import sqlite3

path = r"C:\SQLite\aulas"
banco = sqlite3.connect(path + r"\BDPerfumes.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Perfumes (id interger, nome text, quantidade interger, id_volume_FK integer, id_marca_FK integer, id_fixacao_FK integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Marcas (id interger, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Fixacoes (id interger, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Volumes (id interger, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencia_Perfume (id_essencia_FK interger, id_perfumeFK interger)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencias (id interger, nome text)")