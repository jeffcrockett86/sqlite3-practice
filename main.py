from Table import Table as T
from Row import Row as R
from Cell import Cell as C
from Col import Col

f = open('db.txt', 'rw')
rows = f.readlines()
t = T()
t.add_rows(rows)

# for row in t.rows:
#     c = C()
