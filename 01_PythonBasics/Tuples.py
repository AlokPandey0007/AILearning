#Tuples are the ordered list which are immutable.

#empty Typle
empty_tuple=()
print(type(empty_tuple))

##creating tuple
mixed_tuple=("apple",10.5,20,True)
tuple_fromList=tuple([1,2,3,4,5,6])

#printing tuple
print(mixed_tuple)
print(tuple_fromList)

#access few items from tuple
print(mixed_tuple[2])       #output-20
print(tuple_fromList[1:4])       #output - (2, 3, 4)

#concatenate tuple
concatenated_tuple=mixed_tuple+tuple_fromList     # it will print - ('apple', 10.5, 20, True, 1, 2, 3, 4, 5, 6)
print(concatenated_tuple)

#print the element multiple times
print(mixed_tuple*3)              #output - ('apple', 10.5, 20, True, 'apple', 10.5, 20, True, 'apple', 10.5, 20, True)

#tuple is immutable
#mixed_tuple[1]="Krish"    #Output - we will get error - TypeError: 'tuple' object does not support item assignment


#count perticular element in the tuple
print(mixed_tuple.count(True))         #output=1

#get the index of any element
print(mixed_tuple.index(10.5))       #Output=1


#packing tuple
packed_tuple=10,"hello",10.5
print(packed_tuple)      #output=(10, 'hello', 10.5)


#unpacking tuple
a,b,c=packed_tuple
print(a," ",b," ",c)        #output=10   hello   10.5

#nested Tuple
nested_tuple=((1,2,3),('a','b','c'))
print(nested_tuple[1][1])     #output=b