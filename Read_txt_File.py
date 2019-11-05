# numpy - array and zero matrix
import numpy as np

# List size
count = 0

# txt file (M1 to M5)
maze_file = 'M1.txt'

# open txt
f = open(maze_file)

# File lines stored inside a list
size_measure_list = f.readlines()

# Original lines and columns count
count_lines = len(size_measure_list)
count_columns = len(size_measure_list[0])

# Conlumns count - to remove odd ones
count_columns_2 = (count_columns + 1) / 2
count_columns_2 = int(count_columns_2)

# Zero numpy matrix with original sizes
numbers_matrix_maze = np.zeros(shape=(count_lines, count_columns))

# Fill matrix with numbers: 1 wall, 0 available path, 2 - 3 ~ path end - begin
for e, f in zip(size_measure_list, range(count_lines)):
    for character, g in zip(e, range(count_columns)):
        if character == ' ':
            numbers_matrix_maze[f, g] = 0
        if character == '-':
            numbers_matrix_maze[f, g] = 1
        if character == '+':
            numbers_matrix_maze[f, g] = 1
        if character == '|':
            numbers_matrix_maze[f, g] = 1
        if character == 'S':
            numbers_matrix_maze[f, g] = 2
        if character == 'E':
            numbers_matrix_maze[f, g] = 3

# Number sequence - odd numbers 0 to list.length()
odd_numbers = []
for n in range(0, count_columns-1):
    if (n % 2) != 0:
        odd_numbers.append(n)

# Remove odd columns and the last one (filled with 0)
numbers_matrix_maze = np.delete(numbers_matrix_maze, np.s_[odd_numbers], axis=1)
numbers_matrix_maze = np.delete(numbers_matrix_maze, count_columns_2, axis=1)

# Print result matrix
print(numbers_matrix_maze)