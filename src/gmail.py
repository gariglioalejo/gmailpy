#print "hello world"

import imaplib 		 #Libreria para trabajar con IMAP
import getpass       # 
import datetime      
import email         # parsear email
import email.header  
import pprint        # prettyprint
import re            # regular expressions
import pymysql
 

conn = pymysql.connect(host= 'localhost', user='meliuser', passwd='meli1234', db='meli')
print 'Conexion Exitosa a la DB'
cur = conn.cursor()

mail = imaplib.IMAP4_SSL('imap.gmail.com',993)


username=raw_input("Ingresar E-Mail: ")
password=getpass.getpass()
mail.login(username, password)
print("Autenticacion Exitosa")

mail.list()
mail.select('inbox')

print("Seleccionada la Inbox de gmail")



print("Mails que contienen \"DevOps\":\n")
typ, data = mail.search(None, '(OR TEXT "DevOps" SUBJECT "DevOps")') #'TEXT', '"DevOps"'

for num in data[0].split():
	typ, data = mail.fetch(num, '(RFC822)')
	msg = email.message_from_string(data[0][1])
	print '#%s | Fecha: %s | From: %s | Subject: %s' % (num, msg['Date'], msg['From'], msg['Subject'])
	date_tupla = email.utils.parsedate_tz(msg['Date'])
	date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tupla))
	
	
	try:
		queryInsert = "INSERT INTO meli.tDevOps VALUES(%s,%s,%s)"
		insertArgs = (date, msg['From'], msg['Subject'])
		
		cur = conn.cursor()
		cur.execute(queryInsert, insertArgs)
		
		conn.commit()
		cur.close()

		
	except ValueError:
		print("Error en el Insert")
		cur.close()
	
	   
cur.close()
conn.close()
print("\nE-Mails guardados en la base MySQL")
mail.close()