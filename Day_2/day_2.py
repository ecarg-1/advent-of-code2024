with open("input_2.txt", "r") as file:
    reports_list = file.readlines()
file.close()

#Part 1
total = 0 #total of safe reports
acceptable_distances = [1, 2, 3] 

#tests a report and returns true if it's safe and false if it's not
def report_tester(report): #accepts a list of ints (already formatted report)
    if sorted(report) == report or sorted(report, reverse=True) == report: #if report is all ascending or descending we can continue
        flag = True #flag to see if it passes the next test
        for i in range(len(report)-1): #interates through first - second to last numbers
            distance = abs(report[i]-report[i+1]) #gives abs value of distance between numbers (doesn't matter if ascending or descending)
            if distance not in acceptable_distances: #if not either 1, 2, or 3 apart
                flag = False #did not pass the distance test
                break #break this for loop since it doesn't matter anymore
        if flag is True: #if everything held up, the test passed
            return True
        else:
            return False
        
for report in reports_list:
    report = [int(i) for i in report.split(' ')] #turns string into list of strings, turns list of strings into list of ints
    if report_tester(report):
        total = total + 1
print(total)

#Part 2
safe_reports = 0 #start count at 0
for report in reports_list:
    is_safe = False #assume every report is unsafe until proven
    report = [int(i) for i in report.split(' ')] #turns string into list of strings, turns list of strings into list of ints
    if not report_tester(report): #if it's unsafe
        for i in range(len(report)): #go through each index
            report_popped = report.copy() #copy the report so it's unchanged by pops
            report_popped.pop(i) #start popping indexes 
            if report_tester(report_popped): #runs tester again
                is_safe = True #if at anypoint, the list is safe, breaks the loop and marks it safe
                break
    else:
        is_safe = True
    if is_safe:
        safe_reports = safe_reports + 1 
print(safe_reports)

