from Table import M as M
from Cell import Cell as C
from Row import Row as R
from Col import Col as Col
import random
import sys
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
answer = words[random.randint(0, len(words))]
# m.answer = words[random.randint(0, len(words))]
print('the answer is', answer)

# m.guess = sys.argv[1:][0]
# m.words = words
sys.argv = ['main.py', 'hutch', 'hello', 'there', 'rents']
sys.argv = sys.argv[1:]
print('sys.argv is', sys.argv)



def my_filter(lst, allowed, words=words):
    output = []
    for i in range(len(sys.argv[0])):
        letter = sys.argv[0][i]
        if letter in answer:
            words = filter(lambda word: letter in word, words)
        else:
            continue
    return words


def play(words=words, guess_num=guess_num, guess=sys.argv, allowed=[]):
    while len(sys.argv) > 0 and guess_num < 6:





        # m.guess = sys.argv[1:][0]
        # m.words = words
        # print(m.guess)

        # guess_row = R(parent=m, name=m.guess)
        # for i in range(len(m.guess)):
        #     c = C(parent=guess_row, name=m.guess[i])

        #     guess_row.cells.append(c)

        #make the rest of the rows
        # m.rows = [R(name=row[:-1], parent=m) for row in f2.readlines()]

        #insert the guess row at the top of them
        # m.rows.insert(0, guess_row)

            # it.make_cols()

            # get list of lines in db.txt
        # rows = f.readlines()

        # new_words = []
            #make a new m
        # m2 = M("Template")
        # m2.rows = [R(name='test')]

        # t.rows = [R(parent=t, name=row) for row in t.rows]
        # for row in m.rows[1:]:
        #     row.cells = [C(name=m.rows[0].name[i], parent=row) for i in range(len(m.rows[1:]))]
            # print(row.cells)

            #letters in this list will be used to filter the word list


        # print(m.answer)
        # m.rows.insert(0, guess_row)


        for i in range(5):
            # c = C(name=m.rows[0].name, parent = m.rows[0])
            # m.rows[0].cells.append(c)
            if sys.argv[0][i] in answer:
                allowed.append(sys.argv[0][i])




            # for letter in sys.argv[0]:
            #     if letter in m.answer and letter != m.answer[i]:
            #         c = C(name=letter, parent=sys.argv[0])
            #         c.is_yellow = True
            #         print(letter, 'is yellow')

                #     allowed.append(letter)
                #     # break
                # elif letter in m.answer and letter == m.answer[i]:
                #     c = C(name=letter, parent=m.guess)
                #     c.is_green = True
                #     print(letter, 'is green')
                #     allowed.append(letter)
                #     # break
                # else:
                #     c = C(name=letter, parent=m.guess)
                #     c.is_black = True
                #     print(letter, 'is black')
                    # break
            #filter out all the words if any of their letters are in allowed
        # def my_filter(_words):
        #     for word in _words:
        #         for letter in word:
        #             if letter.lower() in allowed:
        #                 return False
        #             else:
        #                 return True



        # words2 = list(filter(lambda x: x[0] in allowed, m.words))
        # words = list(filter(my_filter, words))
        # print('length of words2 is', len(words2))
        # print('m.words is', words)
            # for word in words:
            #     for letter in word:
            #         if letter not in allowed:
            #             new_words.append(word)

            # new_words = list(set(new_words))
        # words = list(filter(my_filter, words))
        # print(words2)
        # print(' and '.join(allowed), 'not allowed in the original word list')
        # print(f'After your first guess, there are {len(words)} words left')
        allowed = list(set(allowed))
        words = my_filter(words, allowed)
        guess_num += 1
        # print('m.words is', m.words)
        print(f'Current guess is {sys.argv[0]}')
        print('allowed is', allowed)
        print(f'After guess {guess_num} there are {len(list(words))} words left')

        print(allowed, ' are allowed.')
        # play(words2=new_words, guess_num=guess_num)

        """
        >>> m.words = filter(lambda x, i: x[i] not in
        allowed for i in range(len(x)), words)
        """
        # def my_filter(words):
        #     output = []
        #     for i in range(len(words)):
        #         letter = words[i]
        #         if letter in allowed:
        #             return False
        #         else:
        #             return True
        sys.argv = sys.argv[1:]
        return play(words=words, guess_num=guess_num, guess=sys.argv, allowed=allowed)
        # {'guess_num': guess_num, 'allowed': allowed, 'words': words}

play()
