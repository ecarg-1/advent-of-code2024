with open("input_1_1.txt", "r") as file: #opening the input.txt into a variable "file" to be read only (hence the "r")
    
    list1, list2 = [], [] #initializing lists to put each number into
 
    for line in file.readlines(): #reads each line
        list1.append(int(line.split('   ')[0])) #since there are 3 spaces between each number, it splits it there
        list2.append(int(line.split('   ')[1])) #and turns each string into an int
    #Now, each list has the correct numbers
file.close() #We are done with the file now

list1 = sorted(list1) #sorted from least to greatest
list2 = sorted(list2) #puts it in a variable as opposed to list2.sorted() which returns nothing

total = 0 #starting off the total as 0
for n1, n2 in zip(list1, list2): #zip zips puts together each list 
    total = total + abs(n1 - n2) #adds the difference to the total
print(total)