student_data={
    "Aswin":{"roll_no":10,"age":26,"course":"python"},
    "Mathi":{"roll_no":20,"age":22,"course":"Java"}
}
student_data["Mathi"]["phone_no"]=852406737
print(student_data["Mathi"])
print(student_data ["Mathi"].pop("phone_no"))
print(student_data["Mathi"])