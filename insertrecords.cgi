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

def createPersonList():
	#create person list
	people = []
	#add people to the list
	people.append(["John","Reese"])
	people.append(["Harold","Finch"])
	people.append(["Sameen","Shaw"])
	people.append(["Samantha","Groves"])
	return people

def insertPeople(db,cursor,people):
	for each in people:
		sql = "insert into person(firstname,lastname) values('{0}','{1}')".format(each[0],each[1])
		cursor.execute(sql)
	db.commit()



def createDB(db,cursor):
	#creating a new database
	sql = "create database exampledb"
	cursor.execute(sql)
	db.commit()

def createEntity(db,cursor):
	#use the newly created database
	sql = "use exampledb"
	cursor.execute(sql)
	#create a simple entity
	sql = '''create table person
	(personid int not null auto_increment,
	firstname varchar(20) not null,
	lastname varchar(30) not null,
	primary key(personid))'''

	cursor.execute(sql)
	db.commit()

	
def htmlTail():
	print """</body>
		</html>"""


#main program

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		people = createPersonList()
		insertPeople(db,cursor,people)
		# createDB(db,cursor)
		# createEntity(db,cursor)
		#close the connection
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()				