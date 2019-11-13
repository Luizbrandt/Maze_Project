# numpy - array and zero matrix
import numpy as np

# List size
count = 0

# txt file (M1 to M5)
maze_file = 'M2.txt'

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

start_position = []
end_position = []

# Fill matrix with numbers: 1 wall, 0 available path, 2 - 3 ~ path end - begin
for e, f in zip(size_measure_list, range(count_lines)):
    for character, g in zip(e, range(count_columns)):
        if character == ' ':
            # numbers_matrix_maze[f, g] = [e, f, 0]
            numbers_matrix_maze[f, g] = 0
        if character == '-':
            # numbers_matrix_maze[f, g] = [e, f, 1]
            numbers_matrix_maze[f, g] = 1
        if character == '+':
            # numbers_matrix_maze[f, g] = [e, f, 1]
            numbers_matrix_maze[f, g] = 1
        if character == '|':
            # numbers_matrix_maze[f, g] = [e, f, 1]
            numbers_matrix_maze[f, g] = 1
        if character == 'S':
            # numbers_matrix_maze[f, g] = [e, f, 0]
            numbers_matrix_maze[f, g] = 2
        if character == 'E':
            # numbers_matrix_maze[f, g] = [e, f, 0]
            numbers_matrix_maze[f, g] = 3

odd_numbers = []
for n in range(0, count_columns-1):
    if (n % 2) != 0:
        odd_numbers.append(n)

numbers_matrix_maze = np.delete(numbers_matrix_maze, np.s_[odd_numbers], axis=1)
numbers_matrix_maze = np.delete(numbers_matrix_maze, count_columns_2, axis=1)

row_count = np.size(numbers_matrix_maze, 0)
column_count = np.size(numbers_matrix_maze, 1)

for i in range(row_count):
    for j in range(column_count):
        if numbers_matrix_maze[i][j] == 2:
            start_position = (i, j)
            numbers_matrix_maze[i][j] = 0
        if numbers_matrix_maze[i][j] == 3:
            end_position = (i, j)
            numbers_matrix_maze[i][j] = 0