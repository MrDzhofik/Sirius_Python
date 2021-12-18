def print_operation(operation, num_rows = 9, num_column = 9):
    for i in range(1, num_rows + 1):
    	print('\t'.join(map(str, list(map(operation, [i] * num_column, range(1, num_rows + 1))))))


print_operation(lambda x, y: x + y)
