'''
Team dataStorers
Mohammed Jamil, Addison Huang
SoftDev1 pd 6
K16 -- No Trouble
2018-10-05 
'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="ScriptKittys.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def students():
    command = "CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)"           #SQL command to create table for peeps.csv
    c.execute(command)    #run SQL statement
    with open('data/peeps.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)#DictReader creates a reader in which each row is a dictionary with the key being a fieldname.
        for row in reader:
            #print(row['name'],row['age'],row['id'])# Diagnostic print statements
            command2 = "INSERT INTO students VALUES(\""+row['name']+"\","+ row['age']+","+row['id']+")"#concatenation of the data from the csv with the sql command 
            c.execute(command2)#executes the command for each row

def grades():
    command = "CREATE TABLE grades(code TEXT, mark INTEGER, id INTEGER)"          #SQL command to create table for courses.csv
    c.execute(command)    #run SQL statement
    with open('data/courses.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['code'],row['mark'],row['id']) #Diagnosic print statements
            command2 = "INSERT INTO grades VALUES(\""+row['code']+"\","+ row['mark']+","+row['id']+")" #concatenation of the data from the csv with the sql command 
            c.execute(command2)#executes the command for each row

grades()    
students()
#==========================================================

db.commit() #save changes
db.close()  #close database


