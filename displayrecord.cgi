#! /usr/bin/python

import cgi
import mysql.connector as conn

def htmlTop():
	print """Content-Type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>My server-side template</title>
				<body>"""

def connectDB():
	db = conn.connect(host='localhost',port=8889,user='root',passwd='root',db='exampledb')
	cursor = db.cursor()
	return db,cursor

def selectPeople(db,cursor):
	sql = "select * from person"
	cursor.execute(sql)
	#fetch the results as a list
	people = cursor.fetchall()
	return people

def displayPeople(people):
	print "<table border>"
	print "<tr>"
	print "<th>ID</th>"
	print "<th>List Name</th>"
	print "</tr>"
	for each in people:
		print "<tr>"
		print "<td>{0}</td>".format(each[0])
		print "<td>{0}</td>".format(each[1])
		print "<td>{0}</td>".format(each[2])
		print "</tr>"
	print "</table>"
	
def htmlTail():
	print """</body>
		</html>"""


#main program

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		people = selectPeople(db,cursor)
		cursor.close()
		displayPeople(people)
		htmlTail()
	except:
		cgi.print_exception()				