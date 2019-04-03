#!/usr/bin/env python
from cars import cars

print "Content-type:text/html"
print
print '<html>'
print '<head>'
script = '''
<script>
var t;
function refresh() {
    document.getElementById("myDiv").innerHTML += " .";
}

function timer() {
    t = window.setInterval(refresh, 1000);
}

function test() {
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==1) {
            timer();
            document.getElementById("myHead").innerHTML="";
            document.getElementById("myForm").innerHTML="";
            document.getElementById("myDiv").innerHTML="Waiting";
        }
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
            window.clearInterval(t);
            document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET", "buy.py", true);
    xmlhttp.send();
}
</script>
'''
print script
print '</head>'
print '<body>'
print '<div id="myHead"><h1> Buy Cars </h1></div>'
print '<form id="myForm" onsubmit=""return false action="##">'
print '<select id="mySelect" name="cars">'
for car in cars:
    print '<option value="%s">%s</option>'%(car["value"],car["name"])
print '</select>'
print '<input type="button" value="Buy Car" onclick="test()">'
print '</form>'
print '<div id="myDiv"></div>'
print '</body>'
print '</html>'
