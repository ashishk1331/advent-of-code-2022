lines = ""

with open("input.txt", "r") as file:
	lines = [line for line in  file.read().split("\n")]

for input in lines:
	for i in range(len(input) - 14):
		detect = set([j for j in input[i:i+14]])
		if len(detect) == 14:
			print(i + 14)
			break