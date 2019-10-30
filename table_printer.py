def printTable(table):
    colWidths = [0] * len(tableData)
    for column in table:
        longest = 0
        for item in column:
            if len(item) > longest:
                longest = len(item)
        colWidths[table.index(column)] = longest

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carl', 'David'],
             ['dogs', 'cats', 'moose', 'geese']]

printTable(tableData)