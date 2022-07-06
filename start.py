# from Table import M as M
# from Cell import Cell as C
# from Row import Row as R
# from Col import Col as Col
import random
import sys

# import sqlite3
# con = sqlite3.connect('linkme.db')
# cur = con.cursor()
f = open('db.txt', 'r')
f2 = open('wordleAlpha.txt', 'r')
words = f2.read().split('\n')[:-1]
guess_num = 0

# m = M("Wordle")
answer = words[random.randint(0, len(words))]
print('the answer is', answer)

sys.argv = ['main.py', 'hutch', 'hello', 'there', 'rents', 'blade', 'white']
sys.argv = sys.argv[1:]
print('sys.argv is', sys.argv)



# def my_filter(lst, allowed, words=words):
#     output = []
#     for i in range(len(sys.argv[0])):
#         letter = sys.argv[0][i]
#         if letter in answer:
#             words = filter(lambda word: letter in word, words)
#         else:
#             continue
#     return words


def play(words=words, guess_num=guess_num, guess=sys.argv, allowed=[]):
    while len(sys.argv) > 0 and guess_num < 6:
        for i in range(5):
            if sys.argv[0][i] in answer:
                words = list(filter(lambda word: sys.argv[0][i] in word, words))
                allowed.append(sys.argv[0][i])
        allowed = list(set(allowed))
        # words = my_filter(words, allowed)
        guess_num += 1
        # print('m.words is', m.words)
        print(f'Current guess is {sys.argv[0]}')
        # print('allowed is', allowed)
        print(f'After guess {guess_num} there are {len(list(words))} words left')
        print(allowed, ' are allowed.')
        sys.argv = sys.argv[1:]
        return play(words=words, guess_num=guess_num, guess=sys.argv, allowed=allowed)

play()
