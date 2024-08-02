student_data=[
    {
       "Name":"Aswin",
       "roll_no":5,
       "age":21,
       "course":"python"
    },
    {
       "Name":"Shan",
       "roll_no":48,
       "age":20,
       "course":"java"
    }
    
]


def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student["Name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=course_opted
    student_data.append(new_student)
    
add_new_student("Aishu",2,18,"c++")
print(student_data)
