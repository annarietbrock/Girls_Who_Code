list = ["chicken", "pizza", "boneless pizza", "ice cream", "apples", 14, 7, 8, 436, -5.2, 82.6]
#for item in list: #this option prints each item on a separate line

#print(list[3]) this would print a specific item in the list (don't use the for loop)

#print(list) this option would print the list as it is on 1 line with the ""

print(len(list)) #this will print how many items are in the list (1 more than the last index of the list)
                 #length - 1 = last index
                 
newList = [list, "chicken"] #how to print a list inside of a list
for item in newList:
    print(item)
