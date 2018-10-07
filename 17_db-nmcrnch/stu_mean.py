'''
Team Mohammed
Mohammed Jamil, Mohammed Uddin
SoftDev1 pd 6
K17 -- Average
2018-10-09
'''
import sqlite3


DB_FILE="studentdata.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def add_row(code,mark,id):
	row = "INSERT INTO courses VALUES('{0}',{1},{2});".format(code,mark,id)
	c.execute(row)
#add_row('lunch',102.5,7)
get_peeps = "SELECT * FROM peeps;"
people = c.execute(get_peeps).fetchall()#fetchall is a method for the cursor object that gets all the rows that match the conditional in the select command

create_command = "CREATE TABLE peeps_avg(id INTEGER, average INTEGER);"
c.execute(create_command)

for student in people: #people is a tuple of tuples
	get_grades = "SELECT mark FROM courses WHERE courses.id == {0}".format(student[2]) #student[2] is the id of a student 
	grades = c.execute(get_grades).fetchall() 
	#print (grades)
	total = 0.0
	num = len(grades) #gets the number of grades for each student
	for grade in grades:  #grade is a tuple with only the grade for one subject inside
		total += grade[0] #this gets that grade
	avg = total/num
	print ("student {0} with id {1} has average {2}".format(student[0], student[2], avg)) #print name + id + avg
	insert = "INSERT INTO peeps_avg VALUES({0},{1});".format(student[2],avg) #insert the ids and averages into the table 
	c.execute(insert)

db.commit()
db.close()


	


