import sys
#recursion is calling function inside same function

def factorial(n):
    if(n<2):
        return 1
    else:
        return factorial(n-1)*n

print(factorial(4))


# to know the limit or set the recursion limit use below method by default the limit is 1000
sys.getrecursionlimit()
sys.setrecursionlimit(2000)
