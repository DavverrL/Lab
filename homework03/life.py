import random
import pygame
from pygame.locals import *


class GameOfLife:
    """ Класс для работы с полем и выведением его на экран"""

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width  # Ширина
        self.height = height  # Высота
        self.cell_size = cell_size  # Размер клетки

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self) -> None:  #Запуск
        """ Запустить игру """
        pygame.init()  # Инициализация(создание)
        clock = pygame.time.Clock()  # Время и частота кадров
        pygame.display.set_caption('Game of Life')  # Доступ к дисплею
        self.screen.fill(pygame.Color('white'))  # Цвет экрана
        clist = self.cell_list()  # Размер кл
        running = True  # Цикл игры
        while running:
            for event in pygame.event.get():  # Открывается при запуске получает события из очереди
                if event.type == QUIT:  # Выход через нажатие на Х
                    running = False

            self.draw_cell_list(clist)  # Рисование клеток
            self.draw_grid()
            clist = self.update_cell_list(clist)
            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            pygame.display.flip()  # Обновлние содержимого экрана
            clock.tick(self.speed)  # Частота обновления цикла
        pygame.quit()  # Выход

    def cell_list(self, randomize: bool = True) -> list:
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        if not randomize:  # no Живая
            self.clist = [[0 for col in range(self.cell_width)] for row in range(self.cell_height)]
        else:
            self.clist = [[random.randint(0, 1) for col in range(self.cell_width)] for row in range(self.cell_height)]  # Случайное число в заданном диапозоне
        return self.clist  # Возвращаем отрисовку клеток

    def draw_cell_list(self, clist: list) -> None:
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for rown, row in enumerate(self.clist):  # Возвращает изменяет, при каждом проходе цикла/строка
            for coln, col in enumerate(row):  # Столб
                if col == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     (coln * self.cell_size, rown * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (coln * self.cell_size, rown * self.cell_size, self.cell_size, self.cell_size))

    def get_neighbours(self, cell: tuple) -> list:
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        row, col = cell
        neighbours_positions = [(row - 1, col - 1), (row, col - 1), (row + 1, col - 1), (row - 1, col), (row + 1, col),
                                (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]  # Все возможные верианты
        for neighbour_pos in neighbours_positions:
            row, col = neighbour_pos
            if -1 < row < self.cell_height and -1 < col < self.cell_width:
                neighbours.append(self.clist[row][col])
        return neighbours

    def update_cell_list(self, cell_list: list) -> list:
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = [[0 for col in range(self.cell_width)] for row in range(self.cell_height)]
        for rown, row in enumerate(cell_list):
            for coln, col in enumerate(row):
                neighbours = self.get_neighbours((rown, coln))
                neighbours_num = neighbours.count(1)
                if neighbours_num == 3 or (neighbours_num == 2 and col == 1):
                    new_clist[rown][coln] = 1
        self.clist = new_clist
        return self.clist


if __name__ == '__main__':
    game = GameOfLife(800, 600, 20)
    game.run()