# table_printer.py
# automatetheboringstuff.com Chapter 6
# Vikram Sehgal
def printTable(strlst):
    finstr = ""
    row_len = len(tableData)
    col_len = len(tableData[0])
    for i in range(col_len):
        for q in range(row_len):
            temp = strlst[q][i].rjust(len(max(strlst[q]))+1)
            finstr = finstr + temp
        finstr = finstr + "\n"
    return finstr

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]
    print(printTable(tableData))