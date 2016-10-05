import random
choose = random.randint
way = random.random
def make_layout(size):
	maze = []
	for i in range(size + 2):
		maze.append([])
		if i == 0 or i == size+1:
			for j in range(size + 2):
				maze[i].append(u'\U0001f604')
		else:
			for j in range(size + 2):
				if j == 0 or j == size + 1:
					maze[i].append(u'\U0001f604')
				else:
					maze[i].append(" ")
	return maze
def incx(maze,i,j):
	j+=1
	maze[i][j] = u'\U0001f604'
	return (i,j)
def incy(maze,i,j):
	i+=1
	maze[i][j] = u'\U0001f604'
	return (i,j)
def decx(maze,i,j):
	j-=1
	maze[i][j] = u'\U0001f604'
	return (i,j)
def decy(maze,i,j):
	i-=1
	maze[i][j] = u'\U0001f604'
	return (i,j)




def fill_the_maze(maze,i,j):
	variants = {
					1: incy,
					2: incx,
					3: decy,
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
			return 0
		ch = ways[choose(0,len(ways)-1)]
		i,j = variants[ch](maze,i,j)










size = int(input())
maze = make_layout(size)
fill_the_maze(maze,1,1)
for i in range(len(maze)):
	try:
		print("".join(maze[i]))
	except:
		print(maze)
		break



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


