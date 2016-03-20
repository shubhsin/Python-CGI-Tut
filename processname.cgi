#! /usr/bin/python

import cgi

def htmlTop():
	print """Content-Type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>My server-side template</title>
				<body>"""

def getData():
	formData = cgi.FieldStorage()
	firstname = formData.getvalue('firstname')
	return firstname

	
def htmlTail():
	print """</body>
		</html>"""


#main program

if __name__ == "__main__":
	try:
		htmlTop()
		firstName = getData()
		print "Hello {0}!".format(firstName)
		htmlTail()
	except:
		cgi.print_exception()				