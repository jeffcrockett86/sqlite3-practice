from Table import Table as T
from Row import Row as R
from Cell import Cell as C
from Col import Col

f = open('db.txt', 'r')
rows = f.readlines()
t = T()
top_row = t.add_row(rows).rows[0]
for cell in t.rows[0]:
    c = C(parent=top_row)
    print(c)
    c.add_content(cell)
    print(c.parent)
    # t.rows[0].cells.append(c)
    print(type(t.rows[0]))
    print("top_row.cells is", cell)

print('top_row is', top_row)

print('rows are', t.rows)

# for row in t.rows.split():
#     print(row)
#     for cell in Row:
#         c = C(parent=row)
#         c.add_content(cell)
