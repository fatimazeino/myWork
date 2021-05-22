# students.py
# This program allows a user to create new students and to view students
# Author: Fatima Zeino

import json
filename = "studentData.json"

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q) :").strip()
    return choice

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    while moduleName != "":
        module = {}
        module["name"]=moduleName
        module["grade"]=int(input("\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def displayModules(modules):
    print("\tName  \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))


def doView(students):
   for currentStudent in students:
       print(currentStudent["name"])
       displayModules(currentStudent["modules"])
       
def doNothing(dumby):
 pass

def savedict(obj):
   with open(filename, 'wt') as f:
        json.dump(obj,f)

def doSave(students):
 #call to save dict here
 savedict(students)
 print("students saved")

def readDict():
    with open(filename) as f:
        return json.load(f)

def doLoad():
  return readDict()


#the dict that maps a letter to function
choiceMap = {
 'a': doAdd,
 'v': doView,
 's': doSave,
 'q': doNothing # q is a valid choice
}
#main program
students = doLoad()
choice = displayMenu()
while(choice != 'q'):
 if choice in choiceMap:
# run the function
  choiceMap[choice](students)
 else: # use did not enter something valid
  print("\n\nplease select either a,v or q")
 choice=displayMenu()


