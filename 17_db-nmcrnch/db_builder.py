
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="studentdata.db"

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
            #insert into tbl values
            insert = "INSERT INTO {0} VALUES('{1}',{2},{3});".format(name,row[field0],row[field1],row[field2])
            c.execute(insert)
table_creator('peeps','peeps.csv','name','age','id')
table_creator('courses','courses.csv','code','mark','id')
#==========================================================

db.commit() #save changes
db.close()  #close database
