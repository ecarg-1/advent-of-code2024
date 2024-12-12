with open("input_3.txt", "r") as file:
    text = file.read()
file.close()

import re
 #Part 1
pattern = r"mul\((\d{1,3}),(\d{1,3})\)" #pattern of mul(any1-3digit, any1-3digit) but only records the strings of numbers (due to parentheses placement)
matches = re.findall(pattern, text) #returns a list of strings
total = 0 #starting off at 0
for x in matches:
    total = total + int(x[0])*int(x[1])
print(total)

#Part 2
new_pattern =  r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))" #looks for do(), don't() or mul(any1-3digit,any1-3digit)
new_match = re.findall(new_pattern, text) #returns a list of strings
cur_flag = True #marks if do or don't has occured
new_total = 0
for str in new_match:
    if str == "don't()":
        cur_flag = False
        continue
    elif str == "do()":
        cur_flag = True
        continue
    if cur_flag is False: #if don't activated the flag, then nothing happens
        continue
    else: #if do is on, then multiplcation happens
        nums = re.findall(pattern, str) #takes out the numbers from the mul(,) string
        new_total = new_total + int(nums[0][0])*int(nums[0][1]) #adds product to total
print(new_total)