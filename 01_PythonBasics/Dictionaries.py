'''Dictionaries are created using curly braces {}. The key is on the left side of the colon (:) 
and the value is on the right. A comma separates each key-value pair. Creating a Python dictionary is straightforward. 
Remember to use curly braces {} and separate each key-value pair with a comma'''


# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict_intKey= {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict_mixedKey= {'name': 'John', 1: [2, 4, 3]}
# using dict()
my_dict_usingDict= dict({1:'apple', 2:'ball'})
# from sequence having each item as a pair
my_dict_AsPair = dict([(1,'apple'), (2,'ball')])


#create Dictionary
student_dict={"name":"Jone","age":20}
print(type(student_dict))        #output=<class 'dict'>
print(student_dict)               #output={'name': 'Jone', 'age': 20}


#add element in dictionary
student_dict["address"]='Chandigarh'
print(student_dict)              #output={'name': 'Jone', 'age': 20, 'address': 'Chandigarh'}


#delete element from dictionary
del student_dict['address']   # it will delete key and value pair
print(student_dict)           #output={'name': 'Jone', 'age': 20}

#print all the keys
keys=student_dict.keys()
print(keys)                  #output - dict_keys(['name', 'age'])

#print all the values
values=student_dict.values()
print(values)             #output - dict_values(['Jone', 20])


#get all key value pair
items=student_dict.items()
print(items)                  #output-dict_items([('name', 'Jone'), ('age', 20)])


#create shallow copy
copy_student=student_dict.copy()         #if we make any change to original dictionary it will not impact the duplicate copy of dictionary.
print(copy_student)


#iterate in dictionary
for key,value in student_dict.items():
    print(key," ",value)

#print values based on key
for key in student_dict.keys():
    print(student_dict[key])


#dictionary comprehension
comp_dict1={x:x*2 for x in range(10)}
print(comp_dict1)    #Output - {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

#dictionary comprehension with condition
comp_dict2={x:x*2 for x in range(10) if x%2==0}
print(comp_dict2)         #output - {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}

#merging dictionary
merged_dict={**comp_dict1,**comp_dict2}
print(merged_dict)                  #it will merge Output - {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
