def reduced_row_echelon_form(matrix):

	pivot = 0															# Tracks pivot element index
	back_swap = len(matrix)-1											# To move any rows containing zeroes to the end of the matrix
	m = len(matrix)														# Number of rows
	n = len(matrix[0])													# Number of columns

	for r in range(m):													# Loop through each row
		scan_r = r 														# scan_r allows look-ahead for rows with non-zero pivot
		while matrix[scan_r][pivot] == 0:								# While the current row has a zero pivot element,
			scan_r += 1													# We increment our look-ahead row counter
			if scan_r == m:												# If we hit the end of the end of the matrix, then we know that all the rows contains a zero at that pivot index.
				scan_r = r 												# So we start from the same row, but now we look for non-zero pivot in the next column.
				pivot += 1
				if pivot == n:											# If pivot == number of columns, stop. We are done. We hit the end of the matrix.
					return												
		matrix[r], matrix[scan_r] = matrix[scan_r], matrix[r]			# scan_r now has the index of non-zero pivot row. Swap raw r with scan_r row.
		pivot_element = matrix[r][pivot]								# Get  the pivot element
		for i in range(n):												# We divide all the numbers in that row by the pivot element, to make our pivot element = 1	
			matrix[r][i] /= pivot_element
		for i in range(m):												# Then loop through all the other rows
			if i != r:													# Ensures we don't reduce the pivot row with pivot row
				factor = matrix[i][pivot]								# Factor is the number by which we need to multiply our pivot row in order to reduce row i
				for j in range(n):										# Subtract all the elements in row i by factor * corresponding element in our pivot row
					matrix[i][j] -= factor*matrix[r][j]
		pivot += 1														# Increment our pivot since we will now move to the next row

if __name__ == '__main__':
	matrix = []
	rows = int(input("How many rows? "))
	print("Enter rows one by separated by space.")
	for _ in range(rows):
		matrix.append(list(map(float, (input().split(" ")))))
	reduced_row_echelon_form(matrix)
	for i in matrix:
		for j in i:
			print(f'{j:0.4f}', end='\t')
		print()