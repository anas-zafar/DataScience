#Question9
students = []
ListScore = []
Masterlist = []
for j in range(0,3):
    name = input("Please enter name of student: ")
    students.append(name)
    for i in range(0,6):
        Gpa = float(input("Please enter gpa: "))
        ListScore.append(Gpa)
        new_students = students.copy()
        new_list_score = ListScore.copy()
    Masterlist.append(new_students)
    Masterlist.append(new_list_score)
    del ListScore[:]
    del students[:]
print(Masterlist)











