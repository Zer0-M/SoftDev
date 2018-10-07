
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def table_creator(name,filename,field0,field1,field2):
    create_command="CREATE TABLE {0}({1} TEXT, {2} INTEGER, {3} INTEGER);".format(name,field0,field1,field2)
    c.execute(create_command)
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #insert into tbl values(name,age,id);
            pop = "INSERT INTO {0} VALUES('{1}',{2},{3});".format(name,row[field0],row[field1],row[field2])
            c.execute(pop)
table_creator('peeps','peeps.csv','name','age','id')
table_creator('courses','courses.csv','code','mark','id')
#command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"        #build SQL stmt, save as string
#c.execute(command)

#with open('peeps.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
        #insert into tbl values(name,age,id);
#        pop = "INSERT INTO peeps VALUES('{0}',{1},{2});".format(row['name'],row['age'],row['id'])
#        c.execute(pop)

#command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"        #build SQL stmt, save as string (same as for peeps)
#c.execute(command)

#with open('courses.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
        #insert into tbl values(courses,mark,id);
#        pop = "INSERT INTO courses VALUES('{0}',{1},{2});".format(row['code'],row['mark'],row['id'])
#        c.execute(pop)

#==========================================================

db.commit() #save changes
db.close()  #close database
