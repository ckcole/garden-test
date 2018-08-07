

# Test case
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

def find_center(matrix):
    '''
    Return an x,y coord thats either the dead center of the matrix,
    or the largest of all the center cells.
    '''
    # find the middle y coord.
    if len(matrix) % 2 == 1:
        y = len(matrix) / 2
    else:
        y = (len(matrix) / 2 - 1, len(matrix) / 2)
    # and the x coord
    if len(matrix[0]) % 2 == 1:
        x = len(matrix[0]) / 2
    else:
        x = (len(matrix[0]) / 2 - 1, len(matrix[0]) / 2)

    if type(x) == int and type(y) == int:
        return (x, y)

    #  if neither has a middle,  get all four center cells
    if type(y) == tuple and type(x) == tuple:
        middle_cells = [(x[0], y[0]), (x[1], y[0]), (x[0], y[1]), (x[1], y[1])]
        largest_value = -1
        # find the largest cell of the four
        for cell in middle_cells:
            if matrix[cell[0]][cell[1]] > largest_value:
                largest_value = matrix[cell[0]][cell[1]]
                largest_cell = cell
        return largest_cell


if __name__ == '__main__':
    print find_center(garden3)
