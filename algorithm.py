list = [-1, 2, 5, 8, 9, 10, 12, 15, 17]

input = list.index(10)



a = len(list) - 1
b = 0


middleNum = a+b//2

numberIsFound = False

while(numberIsFound == False):
    if(input == middleNum):
        numberIsFound = True
        print(input)
    elif(input > middleNum):
        b = middleNum
        middleNum = (a+b)//2

    else:
        a = middleNum
        middleNum = (a+b)//2
