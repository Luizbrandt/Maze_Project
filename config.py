from Read import row_count, column_count, start_position, end_position
from Switch import switch

WINDOW_TITLE = "PathFinder - Algoritmo Genético"

MAZE_WIDTH = column_count
MAZE_HEIGHT = row_count
BLOCK_SIZE = switch(MAZE_HEIGHT)

GENERATIONS = 100
POPULATION_SIZE = 100
MUTATION_RATE = 0.05

START_COORDS = start_position
END_COORDS = end_position
