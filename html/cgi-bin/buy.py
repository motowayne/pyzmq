#!/usr/bin/env python
import cgi
import time

time.sleep(5)

form = cgi.FieldStorage()

car = form.getvalue('cars')

print "Content-type:text/html"
print
print "<html>"
print "<body>"
print "<h1> I want to buy %s </h1>"%car
print "</body>"
print "</html>"
