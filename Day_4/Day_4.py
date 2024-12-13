with open("input_4.txt", "r") as file:
    test = [line.strip('\n') for line in file.readlines()] #reads rows without the \n
file.close()
with open("test_case_10x10.txt", "r") as file:
    case = [line.strip('\n') for line in file.readlines()] #reads rows without the \n
file.close()

#transposes the letters
def transpose(rows):
    transposed_search = [] 
    for i in range(len(rows[0])): 
        word = ''
        for char in rows:
            word = word + char[i]
        transposed_search.append(word)
    return transposed_search

def count_rows(search): #counts XMAS or SAMX in a row
    total = 0
    for row in search:
        total = total + row.count('XMAS') + row.count('SAMX')
    return total

def shift_down(search, row): #shifts rows to make diagonals in a column (both left and right)
    #shift left
    searchL = []
    searchL.append(search[row])
    for i in range(1, 4):
        searchL.append(search[row+i][i:]+i*'F')

    #shift right
    searchR = []
    searchR.append(search[row])
    for i in range(1, 4):
        searchR.append(i*'F'+search[row+i][:-i])
    return searchR, searchL

total = 0
# every row left and right
total = total + count_rows(test)

# every column up and down
total = total + count_rows(transpose(test))

# diagonals
for row_num in range (0, len(test)-3):
    sr, sl = shift_down(test, row_num)
    total = total + count_rows(transpose(sr))
    total = total + count_rows(transpose(sl))

print(total)

#Part 2
def index_a(row): #returns a list of indexes that have 'A' in a given row since 'A' is always the center of X-MAS
    list_a = []
    for i in range(len(row)):
        if row[i]=='A':
            list_a.append(i)
    return list_a

def mas(search, row_num):
    topR_botL, topL_botR = [], []
    ind_A = index_a(search[row_num])
    for i in range(-1, 2):
        #int((i+abs(i))/2) for values of -1, 0, 1 outputs 0, 0, 1
        #int((-i+abs(i))/2) for values of -1, -, 1 outputs 1, 0, 0
        topR_botL.append('F'*-i+search[row_num+i][int((i+abs(i))/2):len(search[0])-int((-i+abs(i))/2)]+'F'*i)
        topL_botR.append('F'*i+search[row_num+i][int((-i+abs(i))/2):len(search[0])-int((i+abs(i))/2)]+'F'*-i)
    t_topr_botr, t_topl_botr = transpose(topR_botL), transpose(topL_botR)
    count = 0
    for ind in ind_A:
        if (t_topl_botr[ind] == 'MAS' or t_topl_botr[ind] == 'SAM') and (t_topr_botr[ind] == 'MAS' or t_topr_botr[ind] == 'SAM'):
            count = count + 1
    return count

count = 0
for i in range(1, len(test)-1):
    count = count + mas(test, i)
print(count)