#def greet(name,dept,subject='python):
#    print(f"Hi {name}")
 #   print(f"Do you teach {'Subject'}?")
  #  print(f"Are you from {dept} department?")
    
#greet("Aswin","IT")


def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")
add(5,7,9)
add(1,2,3,4,5,6,9)
        