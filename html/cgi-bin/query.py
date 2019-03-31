#!/usr/bin/env python
from cars import cars

print "Content-type:text/html"
print
print '<html>'
print '<body>'
print '<h1> Buy Cars </h1>'
print '<form action="buy.py">'
print '<select name="cars">'
for car in cars:
    print '<option value="%s">%s</option>'%(car["value"],car["name"])
print '</select>'
print '<input type="submit">'
print '</form>'
print '</body>'
print '</html>'
