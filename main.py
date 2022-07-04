from Table import Table as T
from Row import Row as R
from Cell import Cell as C
from Col import Col

f = open('db.txt', 'r')

# get list of lines in db.txt
rows = f.readlines()

#make a new table
t = T()

#the top row has the labels for each column
top_row = t.add_row(rows).rows[0]

# add labels to columns, t.rows[0] is the top row
for cell in t.rows[0]:
    c = C(parent=cell, name=cell.split('\\')[0])
    print(c)
    c.add_content(cell)
    print(c.parent)
    # t.rows[0].cells.append(c)
    print(type(t.rows[0]))
    print("top_row.cells is", cell)
    bin = []
    for x in [row for row in t.rows][0]:
        t.rows.append(x.split('/t'))
    print(t.rows)
    for item in t.rows:
        print(item[0])

    # cells = [C(name=label, parent=item[0])for label in [item[0] for item in t.rows[0]]]
    # t.rows[0].cells.append(cells)
    # print(cells)
    # item[0].cells = cells
    """
>>> for x in [row for row in t.rows][0]:
...   bin.append(x.split('/t'))
...
>>> bin
[['NAME\tAGE_YRS\tBREED\tWEIGHT_LBS\tMICROCHIPPED\n'], ['Callie\t1\tCorgi\t16\tno\n'],
['Charley\t1.5\tBasset Hound\t25\tno\n'], ['Jaxon\t0.4\tBeagle\t19\tyes\n']]
    """

print('top_row is', top_row)

print('rows are', t.rows)

# for row in t.rows.split():
#     print(row)
#     for cell in Row:
#         c = C(parent=row)
#         c.add_content(cell)
