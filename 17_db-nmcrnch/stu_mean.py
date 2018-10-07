
import sqlite3


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

command = "SELECT * FROM peeps;"
people = c.execute(command).fetchall()

command = "CREATE TABLE peeps_avg(id INTEGER, average INTEGER);"
c.execute(command)

for student in people: #people is apparently a tuple of tuples
	command = "SELECT mark FROM courses WHERE courses.id == {0}".format(student[2]) #student[2] is id of student 
	grades = c.execute(command).fetchall()
	total = 0.0
	num = 0
	for grade in grades:  #grade is a tuple with only 1 thing inside
		total += grade[0] #gets that 1 thing 
		num += 1
	avg = total/num
	print "student {0} with id {1} has average {2}".format(student[0], student[2], avg) #print name + id + avg
	command = "INSERT INTO peeps_avg VALUES({0},{1});".format(student[2],avg)
	c.execute(command)

db.commit()
db.close()


	


