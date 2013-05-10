#!/usr/bin/env python
import cgitb
import cgi
import sys
cgitb.enable()
import MySQLdb

# Make the connection
connection = MySQLdb.connect(host='host-ip',user='username',passwd='password',db='database_name')

sql = "call getQuote()"

# Run query and get result
try:
  cursor = connection.cursor()
	cursor.execute(sql)
	result = cursor.fetchone()
except Exception, e:
	print e


print "Content-Type: text/html"
print
print """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="EN" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="content-type" content="text/xml; charset=utf-8" />
</head>
<body>
<p>"""
print result[1]
print """\
</p>
</body>
</html>"""

