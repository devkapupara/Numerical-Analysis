a = [
	[1,2,1,2,1],
	[2,1,2,1,2],
	[0,1,0,1,0]
]

pivot = 0

for r, row in enumerate(a):
	pivot_element = row[pivot]
	if pivot_element != 0:
		for i in range(len(row)):
			row[i] = row[i]/pivot_element
		for i in range(len(a)):
			if i != r:
				factor = a[i][pivot]
				for j in range(len(a[i])):
					a[i][j] = a[i][j] - factor*row[j]
	# else:
	# 	if 
	pivot += 1

print(a)
