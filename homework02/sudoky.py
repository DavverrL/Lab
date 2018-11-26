import random
from typing import Tuple, List, Set, Optional


def read_sudoku(puzzle: str) -> List[List[str]]:
    """ to read file sudoku.txt """
    digits = [reader_var for reader_var in open(puzzle).read() if reader_var in '123456789.']
    grid = group(digits, 9)
    return grid


def display(grid: List[List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(grid[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values: List[str], n=9) -> List[List[str]]:
    """
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    a1 = []
    a2 = []
    for i in range(len(values)):
        a1.append(values[i])
        if (i + 1) % n == 0:
            a2.append(a1)
            a1 = []
    return a2


def get_row(values: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos
    return values[row]


def get_col(values: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    gcol = []
    row, col = pos
    for row in range(len(values)):
        gcol += values[row][col]

    return gcol


def get_block(values, pos):
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    block = []
    if(pos[0] < 3) and (pos[1] < 3):
        for i in range(3):
            for j in range(3):
                block += values[i][j]
    elif(pos[0] < 3) and (6 > pos[1] >= 3):
        for i in range(3):
            for j in range(3, 6):
                block += values[i][j]
    elif(6 > pos[0] >= 3) and (pos[1] < 3):
        for i in range(3, 6):
            for j in range(3):
                block += values[i][j]
    elif(6 > pos[0] >= 3) and (9 > pos[1] >= 6):
        for i in range(3, 6):
            for j in range(6, 9):
                block += values[i][j]
    elif(9 > pos[0] >= 6) and (9 > pos[1] >= 6):
        for i in range(6, 9):
            for j in range(6, 9):
                block += values[i][j]
    return block


def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    """
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    emp = 0
    for row in range(len(grid)):
        for col in range(len(grid)):

            if grid[row][col] == '.':
                return tuple([row, col])
            else:
                emp += int(grid[row][col])
    if emp == 405:
        return (-1, -1)


def find_possible_values(grid: List[List[str]], pos: Tuple[int, int]) -> Set[str]:
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> set(values) == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> set(values) == {'2', '5', '9'}
    True
    """
    p = []
    a = set('123456789')
    gbl = set(get_block(grid, pos))
    gcol = set(get_col(grid, pos))
    grow = set(get_row(grid, pos))
    poss = a - gbl - gcol - grow
    for i in poss:
        row = 0
        block = 0
        col = 0
        m = int(i)
        for j in get_row(grid, pos):
            if j != '.':
                row += int(j)
                r = row
        for j in get_col(grid, pos):
            if j != '.':
                col += int(j)
                c = col
        for j in get_block(grid, pos):
            if j != '.':
                block += int(j)
                bl = block
        if((row + m) and (col + m) and (block + m)) < 50:
            p.append(i)
    return p


def solve(grid: List[List[str]]) -> Optional[List[List[str]]]:
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    pos = find_empty_positions(grid)
    if pos == (-1, -1):
        return grid

    p_v = find_possible_values(grid, pos)
    for i in p_v:
        grid[pos[0]][pos[1]] = i
        answer = solve(grid)
        if answer:
            return answer
    grid[pos[0]][pos[1]] = '.'
    return None


def check_solution(solution: List[List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    grid = solution
    i = []
    for row in range(len(grid)):
        for col in range(len(grid)):
            i += grid[row][col]
        if set(i) != set('123456789'):
            return False
    return True


def generate_sudoku(N: int) -> List[List[str]]:
    """
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    gen = 81 - N
    i = 0
    grid = solve([['.']*9 for i in range(9)])
    k = 0
    while k < gen:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != '.':
            grid[row][col] = '.'
            k += 1
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
