print("welcome to my computer Quiz!")

playing = input("Do you want to play? ")

if playing!="yes":
   quit()

print("okay! Let's play:) ")
score=0

answer= input("What does cpu stand for? ")
if answer =="central processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect")

answer= input("What does Gpu stand for? ")
if answer =="Graphical processing unit":
    print('correct!')
    score += 1
else:
    print("incorrect")
    
answer= input("What does gui stand for? ")
if answer =="graphical user interface":
    print('correct!')
    score += 1
else:
    print("incorrect")
    
answer= input("What does psu stand for? ")
if answer =="power supply":
    print('correct!')
    score += 1
else:
    print("incorrect")
    
print("You got " + str(score)+ "Question correct!")
print("You got " + str((score / 4)* 100) + "%.")
