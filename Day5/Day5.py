
f = open('input.txt', 'r')
rules = [[int(num) for num in line.strip('\n').split('|')] for line in f.readlines() if '|' in line]    #all the rules found because they contain '|'                                
f.seek(0,0) #resets the curor from readlines
updates = [[int(num) for num in line.strip('\n').split(',')] for line in f.readlines() if '|' not in line and line.strip('\n')] #all the updates because they do not contain '|' and are not an empty line
f.close()
def validate(update:list): #takes in an update and if it is already valid, totals the middle number. if invalid, validates it and then totals the middle number to a different total
    invalid_ct = 0 #counts invalidities, 0 means it goes toward total1 and anything else means it goes toward total2
    while True: #runs until the update is valid
        valid = True #the update starts as valid and it searches for invalidities
        for rule in rules: #goes through each rule to check for anything out of order
            if rule[0] in update and rule[1] in update: #only checks rules where both pages are in the update
                ind_1, ind_2 = update.index(rule[0]), update.index(rule[1]) #indices of the 2 pages in the rule
                if ind_1 > ind_2: #if the first page is after the second page
                    valid, invalid_ct = False, invalid_ct + 1  #it's invalid and the invalid count increments
                    popped = update.pop(ind_1) #then it reorders it to make it valid for that rule by popping the first page
                    update.insert(ind_2, popped) #and putting it before the second page
        if valid: #once it's valid
            if invalid_ct == 0: totals[0] += update[len(update)//2] #if it was always valid, it totals it in totals[0] by adding whatever num is in the middle index
            else: totals[1] += update[len(update)//2] #if it was validated, it totals it to totals[1] using the same method
            break #breaks the while loop

totals = [0, 0] #made this a list so I could update it from within the function
for update in updates: validate(update) #goes through each update
print('Part 1:',totals[0], '\nPart 2:', totals[1])

