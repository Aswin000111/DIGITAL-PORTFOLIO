student_marks={
        "aswin":98,
        "prasanth":78,
        "mathi":56,
        "rajesh":41,
        "aishu":99,
        "dhana":34
}
student_grades={}
 
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]= "A+"
    elif marks>80:
        student_grades[student]= "A"
    elif marks>70:
         student_grades[student]= "B+"    
    elif marks>60:
         student_grades[student]= "B"
    elif marks>50:
         student_grades[student]= "C"
    elif marks>40:
        student_grades[student]= "D" 
    else:
        student_grades[student]= "F"
        
print(student_grades)                