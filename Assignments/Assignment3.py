def fatorial(num):
    result=1
    if(num<1):
        print("enter valid number")
        result=0
        return result
    if(num==1):
        result=1
        return result
    if(num>1):
        while(num>1):
            result=result*num
            num=num-1
        return result
    

value=fatorial(10)
print(value)

value=fatorial(0)
print(value)

value=fatorial(1)
print(value)