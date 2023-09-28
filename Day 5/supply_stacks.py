stacks = [[] for _ in range(9)]
moves = []

with open("input.txt", "r") as file:
	inpText = file.read()
	lines = inpText.split("\n")

	for line in lines[:8]:
		for index, value in enumerate([line[x:x+3].strip() for x in range(0, len(line), 4)]):
			if value.startswith('['):
				stacks[index].insert(0, value.strip('[]'))

	for line in lines[10:]:
		words = tuple(int(x) for x in line.split() if x.isnumeric())
		moves.append(words)


for move in moves:
	n, init, to = move
	temp = []
	for _ in range(n):
		temp.insert(0, stacks[init - 1].pop())
	stacks[to - 1].extend(temp)

print(''.join([x[-1] for x in stacks]))