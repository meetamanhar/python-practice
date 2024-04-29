# class Student:
#     name = "dimpal"
# s1 = Student()
# print(s1.name)


# #constructor--- default constructor
# class Student:
#     def __init__(self): #self call constructor
        
#         print("adding new student in database")
# s1=Student()


#parameterized constructor
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = Student("Roshan",45) #<---parameter
# s2 = Student("kartik",25)
# print(s1.name,s1.age,"\n",s2.name,s2.age)


# Q => create student class that takes name and marks of 3 subjects as arguments in constructor.
#thent create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val   
        print("your marks is", sum/3)          
s1 = Student("khilesh dahariya",[34,56,99])
print(s1.name)
s1.get_avg()


