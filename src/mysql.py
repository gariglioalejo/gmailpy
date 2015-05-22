import pymysql
import os

queryDb = "CREATE DATABASE IF NOT EXISTS meli"
queryCreateUser = "CREATE USER 'meliuser'@'localhost' IDENTIFIED BY 'meli1234'"
queryGrantPriv = "GRANT ALL PRIVILEGES ON meli.* To 'meliuser'@'localhost' WITH GRANT OPTION"
querytabla = "CREATE TABLE meli.tDevOps (fecha TIMESTAMP, sender VARCHAR(50), subj VARCHAR(50))"
queryDelete = "DROP DATABASE IF EXISTS meli; GRANT USAGE ON *.* TO 'meliuser'@'localhost'; DROP USER 'meliuser'@'localhost';"

os.system('clear') #Clear en el shell

conn = pymysql.connect(host= 'localhost', user='root', passwd='', db='') #Conectar como root a la DB
print("Conectado como Root")
cur = conn.cursor()

cur.execute(queryDelete) #Borro la base de datos si ya existia
cur.execute(queryDb)
print("Base de Datos Creada")
cur.execute(queryCreateUser)
cur.execute(queryGrantPriv)
print("Usuario meliuser con privilegios creado")
cur.execute(querytabla)
print("Tabla tDevOps creada")

cur.close()
conn.close()
print("Conexion terminada...")





