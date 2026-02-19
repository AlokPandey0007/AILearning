# 1. To Open the file in python
# file1=open("01_PythonBasics/resources/data.txt",'r')  # to open the file

# data=file1.read()
# print(data)
# file1.close()   # to close the file


# 2. To open the file where you don't have to close it explicitly
with open("01_PythonBasics/resources/data.txt",'r') as file2:
    print(file2.read())       # to read all content
    # print(file2.readline())   # To read first line
    # list2= file2.readlines()  # to read all lines and then print one by one
    # for i in list2:
    #     print(i)
    
# it has four mode  'r' - To read , 'w' - to write , 'a' - to append , 'r+' t - to read and write. 
    
#example
with open("01_PythonBasics/resources/data.txt",'r') as file2:
   
    file2.write("alok")  # it will return the number if char written in file
        




