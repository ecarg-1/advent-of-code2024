'''
Using imaginary numbers. The rows are reprented by the real numbers. The columns are represented by the imaginary numbers. 
Directions: -1 = up, j = right, 1 = down, -j = left, to cycle through multiply by -j
'''
f = open('input.txt','r')
grid = {row + col * 1j: line[col] for row, line in enumerate(f.readlines()) for col in range(len(line.strip('\n')))}
start = [pos for pos in grid if grid[pos] == '^'][0] #There will only be 1 start so takes the first item in list as the start

def run(barrier = None): #takes in a barrier and acts like that position is a #
    p, visited, d = start, set(), -1 #position, visted set, direction
    while p in grid and (p , d) not in visited:  #runs as long as the position is in the grid and the postion and direction has not been done before
        visited.add((p, d))  #adds the position and direction to visited
        if p + d not in grid or grid[p+d] != '#' and p + d != barrier: p += d #moves position if p + d is not in the grid, not #, and not the barrier
        else: d *= -1j #otherwise changes direction
    return list(set([item[0] for item in visited])), (p ,d) in visited #returns list of visited places and directions and a boolean if the last position is within the grid

path = run()[0] #gets a list of all visited positions
print('Part 1:', len(path),'\nPart 2:', sum([run(barrier=p)[1] for p in path])) #makes each visited position a barrier and returns the boolean and sums the trues
