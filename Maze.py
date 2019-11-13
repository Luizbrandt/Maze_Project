from random import randint
from Read import numbers_matrix_maze


class Maze:
    # Define walls being black and ways being white
    wallRGB, wayRGB = (0, 0, 0), (255, 255, 255)
    # Offset value for searching near paths along each cell
    offset = [(0, 2), (0, -2), (-2, 0), (2, 0)]

    def __init__(self, width, height):

        # If width or height is even, sums 1 to be odd
        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1

        self.width = width
        self.height = height
        self.FinalMaze = numbers_matrix_maze

        # Randomizes start position, if sx or sy isn't even, sums 1 to be even
        # Valores de sx e sy serão determinados pelas paredes lidas do labirinto
        sx, sy = randint(1, self.width - 2), randint(1, self.height - 2)
        if self.FinalMaze[sx][sy] ==  1:
            self._addWalls(sy, sx)

        # Generate an empty maze
        self.frontier = set()
        self.visited = set()
        self.toDraw = set()
        self.maze = []

        self.visited.add((sy, sx))
        self.toDraw.add((sy, sx))

        for i in range(self.width):
            row = []
            for j in range(self.height):
                if self.FinalMaze[i][j] == 0:
                    row.append(Maze.wayRGB)
                else:
                    row.append(Maze.wallRGB)
            self.maze.append(row)

    def _clamp(self, n, minN, maxN):
        return min(max(minN, n), maxN)

    def _addWalls(self, y, x):
        for o in Maze.offset:
            cell = (y + o[0], x + o[1])
            if self._range(cell[0], cell[1]) and \
                    cell not in self.visited and \
                    cell not in self.frontier and \
                    self.maze[cell[0]][cell[1]] == Maze.wayRGB:
                self.frontier.add(cell)

    def _findVisitedNear(self, y, x):
        return [(o[0] + y, o[1] + x) for o in Maze.offset if (o[0] + y, o[1] + x) in self.visited]

    def _range(self, y, x):
        return 0 <= x < self.width and 0 <= y < self.height

    def getMaze(self):
        return self.maze

    def getFrontier(self):
        return self.frontier

    def getToDraw(self):
        return self.toDraw

    def getColor(self, y, x):
        return self.maze[y][x]

    #
    def workOneStep(self):
        self.toDraw.clear()
        if len(self.frontier) > 0:
            cell = self.frontier.pop()

            near = self._findVisitedNear(cell[0], cell[1])
            inmaze = near[randint(0, len(near) - 1)]

            dy, dx = self._clamp(
                cell[0] - inmaze[0], -1, 1), self._clamp(cell[1] - inmaze[1], -1, 1)

            if dy != 0:
                self.maze[inmaze[0] + dy][inmaze[1]] = Maze.wayRGB
                self.toDraw.add((inmaze[0] + dy, inmaze[1]))
            if dx != 0:
                self.maze[inmaze[0]][inmaze[1] + dx] = Maze.wayRGB
                self.toDraw.add((inmaze[0], inmaze[1] + dx))

            self.visited.add(cell)
            self.toDraw.add(cell)

            self._addWalls(cell[0], cell[1])

    def _quad(self, x, y, w, h, img, color):
        for dy in range(h):
            img[y + dy] += [color for i in range(w)]

    def genImg(self, wb, hb):
        img = [[] for i in range(self.height * hb)]
        tx, ty = 0, 0

        for y in range(self.height):
            for x in range(self.width):
                self._quad(tx, ty, wb, hb, img, self.maze[y][x])
                tx += wb
            ty += hb
        return img