x=int(input("Please enter the factorial you are trying to get"))+1

y=x-1
a=y

z=0

arrayOfNumbers=[]

for i in range (x-1):
    x-=1
    arrayOfNumbers.append(x)
    print(arrayOfNumbers)

for j in range(y):
    while z==0:
        tempFirstNum=arrayOfNumbers[z]
        z+=1
        tempSecondNum=arrayOfNumbers[z]
        tempStorage=tempFirstNum*tempSecondNum
        print(tempStorage)
    z+=1

    if z==y:
        break

    FinalStorage=tempStorage*arrayOfNumbers[z]
    tempStorage=FinalStorage

print(FinalStorage)











