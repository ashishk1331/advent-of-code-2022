from string import ascii_lowercase as small, ascii_uppercase as big

input = []

with open("input.txt", "r") as file:
	inpText = file.read()
	for line in inpText.split("\n"):
		input.append(line.strip())

score = 0

# When find out same element across two halves in the rucksack
# 
# for sack in input:
# 	mid = len(sack) // 2
# 	first, second = set(sack[:mid]), set(sack[mid:])

# 	for i in first:
# 		if i in second:
# 			score += ord(i) - 65 + 27 if i.isupper() else ord(i) - 96
# 			break

for sack in range(0, len(input), 3):
	A, B, C = set(input[sack]), set(input[sack+1]), set(input[sack+2])

	for i in (small + big):
		if i in A and i in B and i in C:
			score += ord(i) - 65 + 27 if i.isupper() else ord(i) - 96
			break

print(score)