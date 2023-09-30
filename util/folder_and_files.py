from os import mkdir

for i in range(7, 25 + 1):
	path = f'../Day {i}' 

	# Create directory for all days {here, days left after 6 days}
	mkdir(path)

	# Also, provide with an empty input.txt file
	with open(path + "/input.txt", "x") as file:
		pass