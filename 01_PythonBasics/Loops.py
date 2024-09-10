
#for loop
for i in range(5):
    print(i)

#with start,end and step
for i in range(2,6,2):
    print(i)

#while loop
    
count=0

while(count<6):
    print(count)
    count+=1

count=0
while(count<50):
    if(count==25):
        print(count)
        break        # break will stop the loop
    count+=1

count=0
while(count<4):    
    if(count==3):
        continue          #countinue will skip that iteration
    print(count)
    count+=1