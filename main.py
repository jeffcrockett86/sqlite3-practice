from Table import Table as T
from Row import Row as R
from Cell import Cell as C
from Col import Col

f = open('db.txt', 'r')

# get list of lines in db.txt
rows = f.readlines()

#make a new table
t = T()


t.rows = [R(parent=t, name=row) for row in rows]
for row in t.rows:
    row.cells = [C(name=t.rows[0].name[i], parent=row) for i in range(4)]
    print(row.cells)


# label_cells = [C(name=name, parent='parent') for name in t.rows[0][0].split('\t')]
# print(label_cells)
# add labels to columns, t.rows[0] is the top row
# for cell in t.rows[0]:
#     c = C(parent=cell, name=cell.split('\\')[0])
#     print(c)
#     # c.add_content(cell)
#     print(c.parent)
#     # t.rows[0].cells.append(c)
#     print(type(t.rows[0]))
#     print("top_row.cells is", cell)
#     for x in [row for row in t.rows][0]:
#         t.rows.append(x.split('/t'))
#     print(t.rows)
#     for item in t.rows:
#         print(item[0])

    # cells = [C(name=label, parent=item[0])for label in [item[0] for item in t.rows[0]]]
    # t.rows[0].cells.append(cells)
    # print(cells)
    # item[0].cells = cells



print('rows are', t.rows)

for row in t.rows:
    row.name = row.name.split('\t')

# for row in t.rows.split():
#     print(row)
#     for cell in Row:
#         c = C(parent=row)
#         c.add_content(cell)
