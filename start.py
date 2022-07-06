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
# answer = words[random.randint(0, len(words))]
answer = 'sever'
print('the answer is', answer)

# sys.argv = ['main.py', 'hutch', 'hello', 'there', 'rents', 'blade', 'white']
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


def determine_color(guess, answer, num=5, words=words):
    allowed = []
    for i in range(5):
        if guess[i] == answer[i]:
            words = list(filter(lambda word: word[i] == answer[i] , words))
            allowed.append(guess[i])
            print(guess[i], 'is green')
        elif guess[i] in answer and guess[i] != answer[i]:
            print(guess[i], 'is yellow')
            allowed.append(guess[i])
    return (words, allowed)

def play(words=words, guess_num=guess_num, guess=sys.argv, allowed=[]):
    while len(sys.argv) > 0 and guess_num < 6:
        # for i in range(5):
        #     if sys.argv[0][i] == answer[i]:
        #         words = list(filter(lambda word: word[i] == answer[i] , words))
        #         allowed.append(sys.argv[0][i])
        #     elif sys.argv[0][i] in answer and sys.argv[0][i] != answer[i]:
        #         print(sys.argv[0][i], 'is yellow')

            #     words = list(filter(lambda word: sys.argv[i] in word and sys.argv[i] in answer and word[i] != answer[i], words))
            #     allowed.append(sys.argv[0][i])
        words, allowed = determine_color(sys.argv[0], answer, 5, words)

        allowed = list(set(allowed))
        # words = my_filter(words, allowed)
        guess_num += 1
        # print('m.words is', m.words)
        print(f'Current guess is {sys.argv[0]}')
        # print('allowed is', allowed)
        print(f'After guess {guess_num} there are {len(list(words))} words left')
        print('Words left: ', '\n\n', words)
        print(' and '.join(allowed), ' are in the answer.')
        sys.argv = sys.argv[1:]
        return play(words=words, guess_num=guess_num, guess=sys.argv, allowed=allowed)

play()
