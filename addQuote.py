#!/usr/bin/env python
import cgitb
import cgi
import sys
cgitb.enable()
import MySQLdb

def printMessage(message='Hello world!'):
  print "Content-Type: text/html"
	print
	print """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.or
g/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xht
ml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><
title>addQuote.py testing</title></head>
"""
	print'<body><p>'+message+'</p></body></html>'


# Get the quote
form  = cgi.FieldStorage()
quote = form.getfirst('wisdom')
#quote = cgi.escape(quote)

# Make the connection
connection = MySQLdb.connect(host='192.168.2.201',user='witty',passwd='I l0ve 
cs1073',db='witty')
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
