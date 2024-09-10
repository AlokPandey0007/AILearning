#LIST - It can store any type of variable. It is denoted by []

#list creation
mixed_list=["apple",'a',20,10.5]

#print list
print(mixed_list)

#read 1 element
print(mixed_list[2])

#read all elements
print(mixed_list)

#read few elements
print(mixed_list[1:3])

#modify elements
mixed_list[1]="banana"    # a will be replace by banana
print(mixed_list)

mixed_list[3:]="Red"    # it will modify the list liek - ['apple', 'banana', 20, 'R', 'e', 'd']
print(mixed_list)


#adding element to exiting list
mixed_list.append("Orange")      #orange will be added at the end
print(mixed_list)

#insert element in middle
mixed_list.insert(2,"papaya")   #papaya will be inserted at 2nd index
print(mixed_list)


#remove element
mixed_list.remove(20)   #element 20 will be removed from list
print(mixed_list)

#remove and return element
poped_el=mixed_list.pop(4)  
print(poped_el)             # e will be removed and printed
print(mixed_list)

#get index of element
print(mixed_list.index("d"))    # it wiill return the index of d

#count particulat element
print(mixed_list.count("d"))

#print length of list
print(len(mixed_list))


#reverse the list
mixed_list.reverse()           # it willl reverse the list
print(mixed_list)

#sort the list
mixed_list.sort()
print(mixed_list)

#list slicing

num_list=[1,2,3,4,5,6,7,8,9,0]

print(num_list[3:6]) #prints from 3 to 6 index
print(num_list[:6])  #print from start till 6
print(num_list[::2])  #print from start to end with different of 2 
print(num_list[::-1])  # print in reverse order

#iterating on list
for item in mixed_list:
    print(item)

# creating a new list with the help fof for   
print([x**2 for x in range(1,5)])

#conditional
newList=[x**2 for x in range(1,10) if x%2==0]
print(newList)
