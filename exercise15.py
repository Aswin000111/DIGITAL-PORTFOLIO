class circle:
    pi=3.14
    def __init__ (self,radius=6):
        self.radius=radius
        self.area=circle.pi * radius * radius
    def get_circumference(self):
        return 2 *circle.pi* self.radius
circle_1=circle(4)
print(f" The circumference of circle 1 is: {circle_1. get_circumference()}")
circle_2= circle(14)
print(f" The circumference of circle 2 is: {circle_2. get_circumference()}")
print(f"The area of circle 1 is :{circle_1.area}")

