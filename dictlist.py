Student_Marks = {
    'alice':85,
    'bob':90,
    'charlie':80,
    'david':82,
}
Student_Name = input('Enter Student Name: ')
if Student_Name in Student_Marks:
    print(f"{Student_Name}'s marks: {Student_Marks[Student_Name]}")
