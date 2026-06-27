num=int(input("Enter the number of students:"))
students = []
for i in range(num):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    city = input("Enter City: ")
   
    student= {
    "name": name,
    "marks": marks,
    "city":city
}
   
    students.append(student)
'''name=input("Enter Name: ")
marks=int(input("Enter Marks: "))
city=input("Enter City: ")
student2={"name": name,
          "marks":marks,
          "city":city}

students.append(student2)'''
for student in students:
    print("========== Student ==========")
    print("Name :", student["name"])
    print("Marks:", student["marks"])
    print("City: ", student["city"])
    print("==============================")
    print()