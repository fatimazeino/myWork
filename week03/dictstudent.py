# dictstudent.py
# This program reads on student information dict and print out her data
# Author: Fatima Zeino

student = {
    "name" : "Mary",
    "modules" : [
        {
          "courseName" : "Programming",
          "grade" : 45
        },
        {
          "courseName" : "History",
          "grade" : 99
        }
    ]
}
print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t {}".format(module["courseName"], module["grade"]))