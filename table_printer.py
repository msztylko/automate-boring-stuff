def printTable(table):
    colWidths = [0] * len(tableData)
    for column in table:
        longest = 0
        for item in column:
            if len(item) > longest:
                longest = len(item)
        colWidths[table.index(column)] = longest

    for i in range(len(table)):
        print()
        for column in table:
            formatted = column[i].rjust(max(colWidths))
            print(formatted, end=' ')


tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carl', 'David'],
             ['dogs', 'cats', 'moose', 'geese']]

printTable(tableData)