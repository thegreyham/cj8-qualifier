from typing import Any, List, Optional
import sys

asciiChars = ["│", "─", "┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘"]

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    #TODO
    # Add label logic
    # clean up to smaller functions

    rowDataDict = {}
    rowMaxLength = {}
    totalCols = len(rows[0])
    count = 0
    while count < totalCols:
        if count not in rowDataDict:
            rowDataDict[count] = []
        for row in rows:
            rowDataDict[count].append(" " + str(row[count]) + " ")
        count += 1

    print(rowDataDict)

    rowNum = 0
    for item in rowDataDict:
        maxLength = get_max_lenght(rowDataDict[item])
        rowMaxLength[rowNum] = maxLength
        rowNum += 1


    # dynamically generate the top table.
    table = ""
    tstart = asciiChars[2]
    tmiddle = asciiChars[3]
    tend = asciiChars[4]
    tfiller = asciiChars[1]
        
    table += tstart
    tableLastLine = asciiChars[8]
    for item in rowMaxLength:
        rowLength = rowMaxLength[item]
        table += tfiller*rowLength
        tableLastLine += tfiller*rowLength
        if rowLength == totalCols:
            table += tend
            tableLastLine += asciiChars[-1]
        else:
            table += tmiddle
            tableLastLine += asciiChars[9]

    table += "\n"
    rowNum = 0
    for row in rows:
        table += add_row(row,rowMaxLength,center=True)
        rowNum+=1

    table += tableLastLine
    print(table)

def get_max_lenght(row):
    maxLength = 0
    for item in row:
        item = str(item)
        if len(item) > maxLength:
            maxLength = len(item)
    return maxLength
    # if labels:
    #     pass #calculate the lenght
    

def add_row(rows,rowMaxLength,center=False):
    """ Adds a row to the table """
    rowString = str(asciiChars[0])
    colNum = 0
    for row in rows:
        #row = str(" " + str(row))
        row = str(row)
        
        maxLength = rowMaxLength[colNum]
        
        if not center:
            row = " " + row
            rowLen = len(row)
            lenDiff = maxLength - rowLen
            if lenDiff > 0:
                row = row + " "*lenDiff
        else:
            row = row.center(maxLength)
        print(row)
        rowString += row
        rowString += asciiChars[0]
        colNum += 1
    return str(rowString+"\n")

def add_label():
    """ Adds the header labels to the table """
    pass


txt = "banana"
txt2 = "jijij"
txt = txt.center(20)
txt += txt2
print(f"txt: {txt}")

make_table(rows=[
               ["Apple", 5, 2],
               ["Banana", 3, "sadfgdsafdsafdsafdsafdsafdsafdsafdsaf"],
               ["Cherry", 7, 4]
           ])
