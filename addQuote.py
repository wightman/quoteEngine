#!/usr/bin/env python
import cgitb
import cgi
import sys
cgitb.enable()
import MySQLdb

# Get the quote
form  = cgi.FieldStorage()
quote = form.getfirst('wisdom')
#quote = cgi.escape(quote)

# Make the connection
connection = MySQLdb.connect(host='host-ip',user='username',passwd='password',db='database_name')
cursor = connection.cursor()

sql = "call addQuote('"+quote+"')"

try:
	cursor.execute(sql)
	connection.commit()
except:
	connection.rollback()
cursor.close()
connection.close()
printMessage("Quote uploaded!")
