input = []

with open("input.txt", "r") as file:
	inpText = file.read()
	for line in inpText.split("\n"):
		input.append(tuple(line.strip().split(" ")))

# When XYZ are interpreted as shapes
#   opponent - your turn = win score + shape
# outcomes = {
	
# 	# all possibilities for rock
# 	('A', 'X'): 3 + 1,
# 	('A', 'Y'): 6 + 2,
# 	('A', 'Z'): 0 + 3,

# 	# all possibilities for paper
# 	('B', 'X'): 0 + 1,
# 	('B', 'Y'): 3 + 2,
# 	('B', 'Z'): 6 + 3,

# 	# all possibilities for scissors
# 	('C', 'X'): 6 + 1,
# 	('C', 'Y'): 0 + 2,
# 	('C', 'Z'): 3 + 3,
# }

# when XYZ are interpreted as outcome of playing
outcomes = {
	
	# all possibilities for rock
	('A', 'X'): 0 + 3,
	('A', 'Y'): 3 + 1,
	('A', 'Z'): 6 + 2,

	# all possibilities for paper
	('B', 'X'): 0 + 1,
	('B', 'Y'): 3 + 2,
	('B', 'Z'): 6 + 3,

	# all possibilities for scissors
	('C', 'X'): 0 + 2,
	('C', 'Y'): 3 + 3,
	('C', 'Z'): 6 + 1,
}


score = 0

for i in input:
	score += outcomes[i]

print(score)