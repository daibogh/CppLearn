import random
random.seed()
choose = random.randint
way = random.random
def make_layout(size):
	maze = []
	for i in range(size + 2):
		maze.append([])
		if i == 0 or i == size+1:
			for j in range(size + 2):
				maze[i].append("#")#u'\U0001f604')
		else:
			for j in range(size + 2):
				if j == 0 or j == size + 1:
					maze[i].append("#")#uu'\U0001f604')
				else:
					maze[i].append(" ")
	return maze
def incx(maze,i,j):
	
	maze[i][j] = u'\U00002192'
	j+=1
	return (i,j)
def incy(maze,i,j):
	
	maze[i][j] = u'\U00002193'
	i+=1
	return (i,j)
def decx(maze,i,j):
	
	maze[i][j] = u'\U00002190'
	j-=1
	return (i,j)
def decy(maze,i,j):
	
	maze[i][j] = u'\U00002191'
	i-=1
	return (i,j)




def fill_the_maze(maze,i,j):
	stack = []
	maze[i][j] = "*"
	stack.append((i,j))

	variants = {
					1: incy,
					2: decy,
					3: incx,
					4: decx
		}
	
	while 1:
		ways = []
		print(i,j)
		if maze[i+1][j] == " ":
			ways.append(1)
		else:
			ways.append(False)
		if maze[i-1][j] == " ":
			ways.append(2)
		else:
			ways.append(False)
		if maze[i][j+1] == " ":
			ways.append(3)
		else:
			ways.append(False)
		if maze[i][j-1] == " ":
			ways.append(4)
		else:
			ways.append(False)
		while 1:
			if False in ways:
				ways.remove(False)
			else:
				break
		if len(ways) == 0:
			if len(stack):
				
				i,j = stack.pop()
				if prev_i == i and prev_j == j:
					return 0
				continue
			else:
				return 0
		ch = ways[choose(0,len(ways)-1)]
		stack.append((i,j))
		prev_i,prev_j = i,j
		i,j = variants[ch](maze,i,j)


def new_fill(maze,size):
	i,j = 0,0
	stack = []
	fingerprints = 1
	while fingerprints < size**2:
		if maze[i+1][j] == " " or maze[i-1][j] == " " or maze[i][j+1] == " " or maze[i][j-1] == " ":
			vars = []
			stack.append((i,j))
			if maze[i+1][j] == " ":
				vars.append(1)
			if maze[i-1][j] == " ":
				vars.append(2)
			if maze[i][j+1] == " ":
				vars.append(3)
			if maze[i][j-1] == " ":
				vars.append(4)


			if len(vars) == 0 and len(stack) == 0:
				return 0
			if  len(vars) == 0:
				i,j = stack.pop()
				continue
			ch = vars[choose(0,len(vars)-1)]
			i,j = variants[ch](maze,i,j)






size = int(input())
maze = make_layout(size)
fill_the_maze(maze,1,1)
f = open("labirint.txt","w")
for i in range(len(maze)):
	# try:
	# 	print("".join(maze[i]))
	# except:
	# 	print(maze)
	# 	break
	f.write("".join(maze[i])+"\n")
f.close()

# for i in range(size):
# 	maze.append([])
# 	for j in range(size):
# 		maze[i].append(" ")

# print(maze)
# def choose_way(maze = maze , i,j):
# 	answer = 4
# 	if i == 0 or j == 0:
# 		if j == 0 and i == 0:
# 			answer -= 2
# 		else:
# 			answer -= 1
# 	if i == len(maze)-1 or j == len(maze)-1:
# 		if i == len(maze)-1 and j == len(maze)-1:
# 			answer -= 2
# 		else:
# 			answer -= 1
# 	if maze[i+1] != " ":
# 		answer -= 1
# 	elif maze[i - 1] 

# i,j = 0,0
# comands = {
# 			1: lambda x: x+1,
# 			2: lambda x: x - 1
# }
# maze[i][j] = u'\U0001f604'
# while 1:
# 	if way():
# 		i = comands[choose(1,2)](i)


