#grades of students
marks = int(input("marks:"))
if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")