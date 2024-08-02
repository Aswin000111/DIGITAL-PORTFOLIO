class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
        
    def display(self,subject_name):
        print(f"Hi, I am {self.name} and I teach {subject_name}")
    
    def update_followers(self,followers_name):
        self.followers +=1
        
instructor_1= Instructor("Aswin","Mathi")
print(instructor_1.name)
instructor_1.display("python")
instructor_1.update_followers("viji")
print(instructor_1.followers)
instructor_2=Instructor("aishu","mathi")
print(instructor_2.followers)

