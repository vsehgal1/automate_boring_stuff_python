# char_pic_grid.py
# automatetheboringstuff.com Chapter 4
# Vikram Sehgal

def grd (lst):
    len_row = len(lst)
    len_column = 0

    # find number of columns in the matrix
    for i in lst[0]:
        len_column += 1
    
    strn = ""
    
    for i in range(len_column):
        for j in range(len_row):
            strn = strn + lst[j][i]
        strn = strn + "\n"

    return strn
    
if __name__ == "__main__":
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
    print(grd(grid))