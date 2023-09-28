input = []

with open("input.txt", "r") as file:
	inpText = file.read()
	for line in inpText.split("\n"):
		input.append([tuple(map(int, x.split("-"))) for x in line.strip().split(",")])

score = 0

for x in input:
	a, b = x

	aset, bset = set([x for x in range(a[0], a[1]+1)]), set([x for x in range(b[0], b[1]+ 1)])

	if aset.intersection(bset):
		score += 1

	# if (b[0] >= a[0] and b[1] <= a[1]) or (a[0] >= b[0] and a[1] <= b[1]):
	#	score += 1

print(score)