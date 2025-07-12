
#Task 1
try:
    num=int(input("enter any number: "))
    if(num%2==0):
        print(str(num) +" is a even number")
    else:
        print(str(num)+" is a odd number")
except:
    print("Please enter valid number")


#Task - 2
sum=0
for i in range(1,51):
    sum=sum+i

print("the sum of number from 1-50 is : "+str(sum))