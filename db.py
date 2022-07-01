

# Skip to content
# Using Gmail with screen readers
# Meet
# New meeting
# Join a meeting
# Hangouts

# Conversations
# 3.72 GB of 15 GB used
# Terms · Privacy · Program Policies
# Last account activity: 0 minutes ago
# Details
# This module contains database functions

import sqlite3
from Table import Table as T
from Row import Row as R

conn = None
cursor = None

def add_rows(self, rows):
    self.rows.append([row for row in rows])
    return self
# Attempt to open the database at the given location.  Return True if successful, False otherwise
def openDatabase(path):
    global conn, cursor
    conn = sqlite3.connect(path)
    if conn == None:
        print("Could not connect to " + path)
        return False
    cursor = conn.cursor()
    return True

# Return true if the given column with the given value exists in the given table
def rowExists(table, column, value):
    sql = "SELECT %s FROM %s WHERE %s = '%s'" % (column, table, column, value.replace("'", "''"))
    # cursor.execute(sql)
    return cursor.fetchone() != None

# Return true if the given two columns with the given values exist in the given table
def rowExists2(table, column1, value1, column2, value2):
    sql = "SELECT %s FROM %s WHERE %s = '%s' AND %s = '%s'" % (column1, table,
            column1, value1.replace("'", "''"), column2, value2.replace("'", "''"))
    # cursor.execute(sql)
    return cursor.fetchone() != None

# Delete rows meeting the given condition from the given table
def delete(table, column, value):
    sql = "DELETE FROM %s WHERE %s = '%s'" % (table, column, value.replace("'", "''"))
    # cursor.execute(sql)

# Like delete but having two columns and two values
def delete2(table, c1, v1, c2, v2):
    sql = "DELETE FROM %s WHERE %s = '%s' AND %s = '%s'" % (table, c1, v1.replace("'", "''"), c2, v2.replace("'", "''"))
    # cursor.execute(sql)

# Insert the given values into the given table
def insert(table, values):
    sql = "INSERT INTO %s VALUES (" % table
    for v in values:
        sql += "'" + v.replace("'", "''") + "',"
    sql = sql[:-1] + ')'
    # cursor.execute(sql)

# insert([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7]], ['option1', 'option2', 'option3', 'option4'])

# select([['1'],['2'],['3'],['4'],], ['1','2','3','4','5','6','7','8','9'])
# Select a single column from the table, subject to the optional '=' conditions.  Return the
# rows as a list of values rather than as a list of one-tuples as they come from sqlite3
def select(table, column, whereCol="", whereVal="", whereCol2="", whereVal2=""):
    sql = "SELECT %s from %s" % (column, table)
    if whereCol != "":
        sql += " WHERE " + whereCol + "='" + whereVal.replace("'", "''") + "'"
    if whereCol2 != "":
        sql += " AND " + whereCol2 + "='" + whereVal2.replace("'", "''") + "'"
    #sql += " ORDER BY " + column
    cursor.execute(sql)
    list = []
    for row in cursor:
        list.append(row[0])
    return list


# Select distinct values from a single column from the table,
# subject to the optional "like" condition.  Return the
# rows as a list of values rather than as a list of one-tuples as they come from sqlite3
# THE CALLER MUST HAVE PRE-TREATED THE WHEREVAL STRING TO ESCAPE ANY % or _ CHARACTERS
# WITH ~, AS APPROPRIATE
def selectDistinctLike(table, column, whereCol="", whereVal=""):
    sql = "SELECT DISTINCT %s from %s" % (column, table)
    if whereCol != "":
        sql += " WHERE " + whereCol + " LIKE '" + whereVal.replace("'", "''") + "' ESCAPE '~'"
    #sql += " ORDER BY " + column
    cursor.execute(sql)
    list = []
    for row in cursor:
        list.append(row[0])
    return list

# Select distinct values from a single column from the table,
# subject to the optional "=" condition.  Return the
# rows as a list of values rather than as a list of one-tuples as they come from sqlite3
def selectDistinct(table, column, whereCol="", whereVal=""):
    sql = "SELECT DISTINCT %s from %s" % (column, table)
    if whereCol != "":
        sql += " WHERE " + whereCol + " = '" + whereVal.replace("'", "''") + "'"
    #sql += " ORDER BY " + column
    cursor.execute(sql)
    list = []
    for row in cursor:
        list.append(row[0])
    return list

def selectCols(table, cols, whereCol="", whereVal="", whereCol2="", whereVal2=""):
    sql = "SELECT "
    for col in cols:
        sql += col + ","
    sql = sql[:-1] + " FROM " + table
    if whereCol != "":
        sql += " WHERE " + whereCol + "='" + whereVal.replace("'", "''") + "'"
    if whereCol2 != "":
        sql += " AND " + whereCol2 + "='" + whereVal2.replace("'", "''") + "'"
    #sql += " ORDER BY "
    for col in cols:
        sql += col + ","
    sql = sql[:-1]
    cursor.execute(sql)
    return cursor.fetchall()

# Update a single column in rows meeting the given condition from the given table
def update(table, column, value, whereCol, whereVal):
    sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s'" % (table, column, value.replace("'", "''"), whereCol, whereVal.replace("'", "''"))
    cursor.execute(sql)

def update2(table, column, value, whereCol, whereVal, whereCol2, whereVal2):
    sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s' AND %s = '%s'" % (table, column, value.replace("'", "''"), whereCol, whereVal.replace("'", "''"), whereCol2, whereVal2.replace("'", "''"))
    cursor.execute(sql)

def commit():
    conn.commit()
# db.py
# Displaying db.py.
