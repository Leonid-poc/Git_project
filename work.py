import pygame

class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def krestiki_noliki(self, screen, num):
        if not self.cell is None:
            self.screen2 = pygame.Surface((self.cell_size, self.cell_size))
            if num == 1:
                pygame.draw.lines(self.screen2, 'blue', False,
                                  [(0, 0), screen.get_size(), (self.cell_size, 0), (0, self.cell_size)], 2)
            else:
                pygame.draw.circle(self.screen2, 'red', (self.cell_size // 2, self.cell_size // 2), self.cell_size // 2)
            screen.blit(self.screen2,
                        (self.left + self.cell_size * self.cell[0], self.top + self.cell_size * self.cell[1]))

    def render(self, screen):
        colors = [pygame.Color('black'), pygame.Color('red'), pygame.Color('blue')]
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen, colors[self.board[y][x]], (x * self.cell_size + self.left,
                                                       y * self.cell_size + self.top,
                                                       self.cell_size, self.cell_size))
                else:
                    self.krestiki_noliki(screen, self.board[y][x])
                pygame.draw.rect(screen, 'white', (x * self.cell_size + self.left,
                                                                    y * self.cell_size + self.top,
                                                                    self.cell_size, self.cell_size), 1)

    def get_cell(self, pos):
        cell_x = (pos[0] - self.left) // self.cell_size
        cell_y = (pos[1] - self.top) // self.cell_size
        if cell_x > self.width - 1 or cell_y > self.height - 1 or cell_x < 0 or cell_y < 0:
            return None
        return cell_x, cell_y

    def get_click(self, mouse):
        self.cell = self.get_cell(mouse)
        if self.cell:
            self.on_click(self.cell)
        else:
            print(self.cell)



    def on_click(self, cell_coords):
        self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 3

def main():
    pygame.init()
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Реакция на события от мыши')
    board = Board(8, 8)
    board.set_view(50, 50, 50)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()