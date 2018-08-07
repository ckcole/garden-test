def find_center(matrix):
    '''
    Return an x,y coord thats either the dead center of the matrix,
    or the largest of all the center cells.
    '''
    # find the middle y coord.
    if len(matrix) % 2 == 1:
        x = len(matrix) / 2
    else:
        x = (len(matrix) / 2 - 1, len(matrix) / 2)
    # and the x coord
    if len(matrix[0]) % 2 == 1:
        y = len(matrix[0]) / 2
    else:
        y = (len(matrix[0]) / 2 - 1, len(matrix[0]) / 2)

    if type(x) == int and type(y) == int:
        return (x, y)

    # inner array is even
    if type(x) == tuple and type(y) == int:
        middle_cells = [(x[0], y), (x[1], y)]
    # outer array is even
    elif type(x) == int and type(y) == tuple:
        middle_cells = [(x, y[0]), (x, y[1])]
    #  if neither has a middle,  get all four center cells
    if type(y) == tuple and type(x) == tuple:
        middle_cells = [(x[0], y[0]), (x[1], y[0]), (x[0], y[1]), (x[1], y[1])]

    largest_value = -1
    # find the largest cell of the middle
    for cell in middle_cells:
        if matrix[cell[0]][cell[1]] > largest_value:
            largest_value = matrix[cell[0]][cell[1]]
            largest_cell = cell
    return largest_cell


def get_largest_adjacent(cell, matrix):
    x, y = cell
    adj = []
    #  Collect all cells to the right, left, above, and below current cell.
    if x != 0:
        adj.append((x - 1, y))
    if y != 0:
        adj.append((x, y - 1))
    if x != len(matrix) - 1:
        adj.append((x + 1, y))
    if y != len(matrix) - 1:
        adj.append((x, y + 1))

    # return the cell with the most carrots.  if all cells are empty,  return None and rabbit sleeps
    largest = 0
    largest_cell = None
    for a_cell in adj:
        if matrix[a_cell[0]][a_cell[1]] > largest:
            largest = matrix[a_cell[0]][a_cell[1]]
            largest_cell = a_cell
    return largest_cell


def run(matrix):
    x, y = find_center(matrix)
    carrots_eaten = matrix[x][y]
    adj = get_largest_adjacent((x, y), matrix)
    while adj is not None:
        carrots_eaten += matrix[adj[0]][adj[1]]
        matrix[adj[0]][adj[1]] = 0
        adj = get_largest_adjacent(adj, matrix)
    return carrots_eaten


# Test cases
garden1 = [
    [5, 7, 8, 6, 3],
    [0, 0, 7, 0, 4],
    [4, 6, 3, 4, 9],
    [3, 1, 0, 5, 8]]

garden2 = [
    [5, 7, 8, 3],
    [0, 0, 7, 4],
    [4, 6, 3, 9],
    [3, 1, 0, 8]]

garden3 = [
    [5, 7, 8, 6, 3],
    [0, 0, 7, 0, 4],
    [4, 6, 3, 4, 9],
    [4, 6, 3, 4, 9],
    [3, 1, 0, 5, 8]]


if __name__ == '__main__':
    test = run(garden1)
    print 'test case returned {}'.format(test)
    if test == 27:
        print 'Passed'
