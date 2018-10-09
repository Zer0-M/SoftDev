'''
Team Mohammed
Mohammed Jamil, Mohammed Uddin
SoftDev1 pd 6
K17 -- Average
2018-10-09
'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="studentdata.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def table_creator(name,filename,field0,field1,field2):
    create_command="CREATE TABLE {0}({1} TEXT, {2} INTEGER, {3} INTEGER);".format(name,field0,field1,field2)#This sql command creates a table using the parameters given
    c.execute(create_command)
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)#The DictReader method turns each row into dictionray with fieldnames as keys 
        for row in reader:
            #The following command will insert the csv data into the table
            insert = "INSERT INTO {0} VALUES(?,?,?);".format(name)
            params=(row[field0],row[field1],row[field2])
            c.execute(insert, params )
table_creator('peeps','peeps.csv','name','age','id')#this creates the table from the peeps csv
table_creator('courses','courses.csv','code','mark','id')#this creates the table from the courses csv
#==========================================================

db.commit() #save changes
db.close()  #close database
