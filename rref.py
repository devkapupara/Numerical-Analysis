def contains_only_zero(row):
	for i in row:
		if i != 0:
			return False
	return True

def reduced_row_echelon_form(matrix):

	pivot = 0																# Tracks pivot element index
	back_swap = len(matrix)-1												# To move any rows containing zeroes to the end of the matrix
	m = len(matrix)															# Number of rows
	n = len(matrix[0])														# Number of columns


	for r, row in enumerate(matrix):										# Loop through each row and keep track of row index
		pivot_element = row[pivot]											# Get  the pivot element
		if pivot_element != 0:												# If pivot element is zero, we can skip that row, otherwise
			for i in range(n):												# We divide all the numbers in that row by the pivot element, to make our pivot element = 1	
				row[i] = row[i]/pivot_element
			for i in range(m):												# Then loop through all the other rows
				if i != r:													# Ensures we don't reduce the pivot row with pivot row
					factor = matrix[i][pivot]								# Factor is the number by which we need to multiply our pivot row in order to reduce row i
					for j in range(n):										# Subtract all the elements in row i by factor * corresponding element in our pivot row
						matrix[i][j] -= factor*row[j]
		pivot += 1															# Increment our pivot since we will now move to the next row

	for i in range(m):														# This loop is just to shift all rows containing zeroes to the end of the matrix, not really needed

		if i < back_swap and contains_only_zero(matrix[i]):					# If our current row < back_swap counter and current row has only zeroes
			matrix[i], matrix[back_swap] = matrix[back_swap], matrix[i]		# Then swap those two rows
			back_swap -= 1													# Decrement our back_swap counter so if we encounter any more rows with zero, we swap it with the correct row from the end.

	return matrix

if __name__ == '__main__':
	a = [
		[2,-2,4,-2],
		[2,1,10,7],
		[-4,4,-8,4],
		[4,-1,14,6]
	]
	a = reduced_row_echelon_form(a)
	for i in a:
		for j in i:
			print(f'{j:0.4f}', end='\t')
		print()