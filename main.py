from Table import Table as T
from Row import Row as R
from Cell import Cell as C
from Col import Col

f = open('db.txt', 'r')
rows = f.readlines()
t = T()
top_row = t.add_row(rows).rows[0]
for cell in top_row:
    c = C(parent=top_row)

# for row in t.rows.split():
#     print(row)
#     for cell in Row:
#         c = C(parent=row)
#         c.add_content(cell)
