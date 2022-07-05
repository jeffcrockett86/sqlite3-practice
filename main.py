# from m import m as T
# from Row import Row as R
# from Cell import Cell as C
# from Col import Col
# from Table import M
# import termcolor
# import sys
# import random
# in this file i will be using find and replace to make all this C hard to read lmao
# maybe i'll get rid of the original if i'm feeling extra devilish muahahaha

from Table import M as M
# from Table import Table as t
from Cell import Cell as C
from Row import Row as R
from Col import Col as Col
import random
"""
>>> from main import *
>>> from m import m as T
>>> from Row import Row as R
>>> from m imprt m as C
  File "<stdin>", line 1
    from m imprt m as C
              ^
SyntaxError: invalid syntax
>>> from m import m as C
>>> from Col import Col
>>>
"""
import sqlite3
con = sqlite3.connect('linkme.db')
cur = con.cursor()
f = open('db.txt', 'r')
f2 = open('wordleAlpha.txt', 'r')
words = f2.read().split('\n')[:-1]
guess_num = 0

m = M("Wordle")
# answer = words[random.randint(0, len(words))]
m.answer = words[random.randint(0, len(words))]
print('the answer is', m.answer)

m.guess = words[random.randint(0, len(words))]
m.words = words
def play(words2=m.words, guess_num=guess_num):
    while len(words2) > 0 and guess_num < 6:






        print(m.guess)
        guess_row = R(parent=m, name=m.guess)
        for i in range(len(m.guess)):
            c = C(parent=guess_row, name=m.guess[i])

            guess_row.cells.append(c)

        #make the rest of the rows
        m.rows = [R(name=row[:-1], parent=m) for row in f2.readlines()]

        #insert the guess row at the top of them
        m.rows.insert(0, guess_row)

            # it.make_cols()

            # get list of lines in db.txt
        # rows = f.readlines()
        not_allowed = []
        new_words = []
            #make a new m
        # m2 = M("Template")
        # m2.rows = [R(name='test')]

        # t.rows = [R(parent=t, name=row) for row in t.rows]
        for row in m.rows[1:]:
            row.cells = [C(name=m.rows[0].name[i], parent=row) for i in range(len(t.rows[1:]))]
            # print(row.cells)

            #letters in this list will be used to filter the word list



        m.rows.insert(0, guess_row)
        for i in range(5):
            c = C(name=m.rows[0].name[i], parent = m.rows[0])
            m.rows[0].cells.append(c)



            for letter in m.guess:
                if letter in m.answer and letter != m.answer[i]:
                    c = C(name=letter, parent=m.guess)
                    c.is_yellow = True
                    print(letter, 'is yellow')
                    not_allowed.append(letter)
                    # break
                elif letter in m.answer and letter == m.answer[i]:
                    c = C(name=letter, parent=m.guess)
                    c.is_green = True
                    print(letter, 'is green')
                    not_allowed.append(letter)
                    # break
                else:
                    c = C(name=letter, parent=m.guess)
                    c.is_black = True
                    print(letter, 'is black')
                    # break
            #filter out all the words if any of their letters are in not_allowed
        def my_filter(_words):
            for word in _words:
                for letter in word:
                    if letter.lower() in not_allowed:
                        return False
                    else:
                        return True


        m.words = list(filter(lambda x: x[0] in not_allowed, m.words))
        print(len(m.words))
            # for word in words:
            #     for letter in word:
            #         if letter not in not_allowed:
            #             new_words.append(word)

            # new_words = list(set(new_words))
        # words = list(filter(my_filter, words))
        # print(words2)
        # print(' and '.join(not_allowed), 'not allowed in the original word list')
        # print(f'After your first guess, there are {len(words)} words left')
        guess_num += 1
        # print('m.words is', m.words)
        print(f'After {guess_num} guess there are {len(m.words)} words left')
        print(not_allowed)
        # play(words2=new_words, guess_num=guess_num)
        return play(words2=m.words, guess_num=guess_num)
        # {'guess_num': guess_num, 'not_allowed': not_allowed, 'words': words}

print(play())
