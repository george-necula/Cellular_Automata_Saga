import pygame

pygame.init()
running = True
window = pygame.display.set_mode((1800, 1000))
cell_width = 2
# rule = int(0b01100110)
rule = 30
cell_count_x = int(window.get_width() / cell_width)
cell_count_y = int(window.get_height() / cell_width)



def grid_draw():
    for i in range(cell_count_x):
        pygame.draw.rect(window, (100, 100, 100), (i * window.get_width() / cell_count_x, 0, 1, window.get_height()))

    for j in range(cell_count_y):
        pygame.draw.rect(window, (100, 100, 100), (0, j * window.get_height() / cell_count_y, window.get_width(), 1))


class Cell:
    def __init__(self, alive=0):
        self.alive = alive

    def rule_check(self, prevoius_cells : list(), rule : int(), index):
        situation = prevoius_cells[index-1].alive*4 + prevoius_cells[index].alive*2 + prevoius_cells[index+1].alive*1 + 1
        # print(situation)
        if '{0:08b}'.format(rule)[-situation] == '1':
            # self.alive = 1
            # print(1)
            return 1
        elif '{0:08b}'.format(rule)[-situation] == '0':
            # self.alive = 0
            # print(0)
            return 0


cell_list = list(Cell(0) for _ in range(cell_count_x))
cell_new_list = list(Cell(0) for _ in range(cell_count_x))
cell_list[int(cell_count_x/2)] = Cell(1)

window.fill((169, 169, 169),)
frame = -1
while running:
    frame += 1
    print('frame number : ', frame)
    # cl = pygame.time.Clock().tick(20)

    if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
        running = False

    if pygame.QUIT in pygame.event.get():
        running = False




    for i in range(1,cell_count_x-1):
        if cell_list[i].alive == 1:
            pygame.draw.rect(window, (10, 10, 10), (
                i * window.get_width() / cell_count_x, frame * window.get_height() / cell_count_y,
                window.get_width() / cell_count_x, window.get_height() / cell_count_y))

        cell_new_list[i].alive = cell_list[i].rule_check(cell_list,rule,i)


    cell_list = cell_new_list
    cell_new_list = list(Cell(0) for _ in range(cell_count_x))

    # running = False

    if frame == cell_count_y :
        comm = input()
        if comm == exit:
            running = False
    grid_draw()
    pygame.display.update()