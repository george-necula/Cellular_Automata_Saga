import pygame

pygame.init()
running = True
window = pygame.display.set_mode((800, 600))
cell_width = 5
cell_count_x = int(window.get_width() / cell_width)
cell_count_y = int(window.get_height() / cell_width)


def grid_draw():
    for i in range(cell_count_x):
        pygame.draw.rect(window, (100, 100, 100), (i * window.get_width() / cell_count_x, 0, 1, window.get_height()))

    for j in range(cell_count_y):
        pygame.draw.rect(window, (100, 100, 100), (0, j * window.get_height() / cell_count_y, window.get_width(), 1))

def drawing_mode(cells_list: list(list())):
    while True:
        window.fill((169, 169, 169))
        grid_draw()

        if pygame.QUIT in pygame.event.get():
            return cells_list
        if pygame.key.get_pressed()[pygame.K_q] == 1:
            return cells_list

        mouse_pos = pygame.mouse.get_pos()

        i, j = [int(mouse_pos[0] / cell_width), int(mouse_pos[1] / cell_width)]
        print('mouse x&y : ', i, j)

        pygame.draw.rect(window, (10, 10, 10), (
            i * cell_width, j * cell_width, cell_width, cell_width))

        if pygame.mouse.get_pressed(3)[0]:
            cells_list[i][j] = Cell(True)
        if pygame.mouse.get_pressed(3)[2]:
            cells_list[i][j] = Cell(False)

        for i in range(cell_count_x):
            for j in range(cell_count_y):

                if cells_list[i][j].alive:
                    pygame.draw.rect(window, (10, 10, 10), (
                        i * cell_width, j * cell_width,
                        cell_width, cell_width))

        pygame.display.update()


class Cell:
    def __init__(self, state: bool = False):
        self.alive: bool = state
        self.new_state: bool = state

    # def __add__(self, other):
    #     return self.alive + other.alive

    def sentence(self, neighbors: int):

        # if neighbors > 0:
        #     print('cell at', i, 'and', j, 'has', neighbors, 'neighbors')

        if self.alive == True and (neighbors < 2 or neighbors > 3):
            self.new_state = False
        if self.alive == False and neighbors == 3:
            self.new_state = True


cells = list(list(Cell(False) for _ in range(cell_count_y)) for _ in range(cell_count_x))

# beacon
# cells[2][2] = Cell(True)
# cells[2][3] = Cell(True)
# cells[3][2] = Cell(True)
#
# cells[5][5] = Cell(True)
# cells[5][4] = Cell(True)
# cells[4][5] = Cell(True)
# -------------

# blinker
# cells[14][5] = Cell(True)
# cells[15][5] = Cell(True)
# cells[16][5] = Cell(True)
# ------------------


# toad
# cells[4][14] = Cell(True)
# cells[5][14] = Cell(True)
# cells[6][14] = Cell(True)
#
# cells[3][15] = Cell(True)
# cells[4][15] = Cell(True)
# cells[5][15] = Cell(True)
# ----------------------


# smallest infinite growth thing

# cells[2+2][10] = Cell(True)
# cells[3+2][10] = Cell(True)
# cells[4+2][10] = Cell(True)
# cells[5+2][10] = Cell(True)
# cells[6+2][10] = Cell(True)
# cells[7+2][10] = Cell(True)
# cells[8+2][10] = Cell(True)
# cells[9+2][10] = Cell(True)
#
# cells[11+2][10] = Cell(True)
# cells[12+2][10] = Cell(True)
# cells[13+2][10] = Cell(True)
# cells[14+2][10] = Cell(True)
# cells[15+2][10] = Cell(True)
#
# cells[19+2][10] = Cell(True)
# cells[20+2][10] = Cell(True)
# cells[21+2][10] = Cell(True)
#
# cells[28+2][10] = Cell(True)
# cells[29+2][10] = Cell(True)
# cells[30+2][10] = Cell(True)
# cells[31+2][10] = Cell(True)
# cells[32+2][10] = Cell(True)
# cells[33+2][10] = Cell(True)
# cells[34+2][10] = Cell(True)
#
# cells[36+2][10] = Cell(True)
# cells[37+2][10] = Cell(True)
# cells[38+2][10] = Cell(True)
# cells[39+2][10] = Cell(True)
# cells[40+2][10] = Cell(True)

# ------------------------


print('entering main loop')
print(cell_count_x, cell_count_y)
i = 0
while running:
    window.fill((169, 169, 169))

    dt = pygame.time.Clock().tick(20)

    if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
        running = False

    if pygame.key.get_pressed()[pygame.K_SPACE] == 1:
        cells = list(list(Cell(False) for _ in range(cell_count_y)) for _ in range(cell_count_x))

    if pygame.key.get_pressed()[pygame.K_1] == 1:
        cells = list(list(Cell(False) for _ in range(cell_count_y)) for _ in range(cell_count_x))
        cells[14][5] = Cell(True)
        cells[15][5] = Cell(True)
        cells[16][5] = Cell(True)

    if pygame.key.get_pressed()[pygame.K_2] == 1:
        cells = list(list(Cell(False) for _ in range(cell_count_y)) for _ in range(cell_count_x))
        cells[4][14] = Cell(True)
        cells[5][14] = Cell(True)
        cells[6][14] = Cell(True)
        cells[3][15] = Cell(True)
        cells[4][15] = Cell(True)
        cells[5][15] = Cell(True)

    if pygame.mouse.get_pressed(3)[0] == 1:
        cells = drawing_mode(cells)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # for i in range(cell_count):
    #     for j in range(cell_count):
    #         cells[i][j].sentence(cells)

    for i in range(1, cell_count_x - 1):
        for j in range(1, cell_count_y - 1):
            neighbors = cells[i-1][j-1].alive + cells[i-1][j].alive + cells[i-1][j+1].alive + cells[i][j-1].alive + \
                        cells[i][j+1].alive + cells[i+1][j-1].alive + cells[i+1][j].alive + cells[i+1][j+1].alive
            cells[i][j].sentence(neighbors)

    for i in range(cell_count_x):
        for j in range(cell_count_y):
            cells[i][j].alive = cells[i][j].new_state

            if cells[i][j].alive:
                pygame.draw.rect(window, (10, 10, 10), (
                i * window.get_width() / cell_count_x, j * window.get_height() / cell_count_y,
                window.get_width() / cell_count_x, window.get_height() / cell_count_y))

    grid_draw()

    pygame.display.update()
