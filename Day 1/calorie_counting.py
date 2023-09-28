input = []

with open("input.txt", "r") as file:
	input = file.read().split("\n") + [""]

# PART 1: max calorie carrying elf
# temp, max_cal = 0, 0

# for cal in input:
# 	if cal == "":
# 		if max_cal < temp:
# 			max_cal = temp
# 		temp = 0
# 	else:
# 		temp += int(cal)

# print(max_cal)

# PART 2: top 3 elfs with max calories
calories = []
temp = 0

for cal in input:
	if cal == "":
		calories.append(temp)
		temp = 0
	else:
		temp += int(cal)

print(sum(sorted(calories, reverse = True)[:3]))