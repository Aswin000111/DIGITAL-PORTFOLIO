#import statistics
#def mean_median_mode(list1):
 #   return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
#print("End of function")

#a,b,c=mean_median_mode([3,5,45,3,2,1,89])
#print(f"mean is {a} \n median is {b} \n mode is {c}")


def add(a,b):
    if a==0 &b==0:
        return " you have entered Zero fot both variables."
    else:
        return a+b
var1=int(input("Enter first variable:\n"))
var2=int(input("Enter second variable:\n"))

result=add(var1,var2)
print(result)