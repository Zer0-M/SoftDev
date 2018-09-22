#Team CodesInSpanish -- Isaac Jon and Mohammed Jamil
#SoftDev1 pd6
#K06 -- Stl/O: Divine your Destiny!
#2018-09-14

import csv, random

def generateDict(file):
    l = [] #List to be filled with occupations and percentage
    with open(file, 'r') as file:
        reader = csv.reader(file)

        next(reader) #Skips heading
        
        for line in reader:
            line[1] = float(line[1]) #Converts percentage to float
            l.append(line) #Adds each pair into list
            
        d = dict(l) #convert list into dictionary

        d.pop("Total")
        
        return d

def getOccupation():
    d=generateDict()
    rng = random.uniform(0,99.8)#random number
    x = 0 #Saves the percentage of the previous occupation 
    for key in d:
        d[key] = d[key] + x #Add previous percentage to current one
        if d[key] > rng:
            return key
        x = d[key] #Updates x
    
        
#=========================================
print(getOccupation())
# Tests to check if percentages were correct
#l=list(generateDict().keys())
#count=[0]*len(l)
#i=0
#x=1000
#while i<x:
#    g=getOccupation()
#    j=0
#    while g!=l[j]:
#        j+=1
#    count[j]+=1
#    i+=1
#print(count)
