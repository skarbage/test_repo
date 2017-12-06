from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name=name
        self.modules=[]
        self.grades={}

    def add_module(self,module):
        self.modules.append(module)
        self.grades[module]=Module.get_grade(module)
        #print(self.grades)
    def get_list_modules(self):
        for el in self.modules:
            print("Modules of Student "+self.name+": "+"\n"+el.get_title())
    def get_grades(self):
        for key in self.grades:
            print("Grades of Student "+self.name+": "+"\n"+key.get_title()+": "+str(key.get_grade()))
                                        #alternativ:        str(key)[8:]    /   str(self.grades[key])
            #oder for keypair in self.grades.items():
                #print("Grades of Student " + self.name + ": " + "\n" + keypair[0].title + ": " + str(keypair[1]))
### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
