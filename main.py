from Table import Table as T
from Row import Row as R
from Cell import Cell as C
from Col import Col
from termcolor import colored
import sys



f = open('db.txt', 'r')
f2 = open('wordleAlpha.txt', 'r')

wt = T("Wordle")

wt.guess = 'rents'
print(wt.guess)
guess_row = R(parent=wt, name="guess_row")
for i in range(len(wt.guess)):
    c = C(parent=guess_row, name=wt.guess[i])
    guess_row.cells.append(c)

#make the rest of the rows
wt.rows = [R(name=row[:-1], parent=wt) for row in f2.readlines()]

#insert the guess row at the top of the table
wt.rows.insert(0, guess_row)

# wt.make_cols()

# get list of lines in db.txt
rows = f.readlines()

#make a new table
t = T("Template")


t.rows = [R(parent=t, name=row) for row in rows]
for row in t.rows[1:]:
    row.cells = [C(name=t.rows[0].name[i], parent=row) for i in range(len(t.rows[1:]))]
    # print(row.cells)

wt.rows.insert(0, guess_row)
for i in range(5):
    c = C(name=wt.rows[0].name[i], parent = wt.rows[0])
    wt.rows[0].cells.append(c)
