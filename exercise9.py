size =input("what size pizza you want(S/M/L)? ")
bill=0
if size == 's' or size =='S':
    bill +=100
    print("Small pizza price is 100 RS. ")
elif size == 'm'  or size =='M':
    bill +=200
    print("Medium pizza price is 200 RS. ")
else:
    bill +=300
    print("Large pizza price is 300 RS. ")

add_pepperoni=input("do you want pepperoni(Y/N)? ")
if add_pepperoni =='Y' or add_pepperoni == 'Y' :
    if size == 'S' or size =='S':
        bill +=30
    else:
        bill +=50
        
extra_cheese=input("Do you want extra cheese(Y/N)? ")
if extra_cheese == 'Y' or extra_cheese =='X':
    bill +=20
print(f"your final bill is {bill}")    

     