import random
import sys

f2 = open('wordleAlpha.txt', 'r')
words = f2.read().split('\n')[:-1]

def wordle(guesses, answer, words=words, allowed=[]):
    if len(guesses) > 0:
        guess = guesses[0]
    if len(guesses)==0:
        return 'That\'s all folks'
    for i in range(5):
        if guess[i] == answer[i]:
            words = list(filter(lambda word: word[i] == answer[i] , words))
            allowed.append(guess[i])
            print(guess[i], 'is green')
        if guess[i] in answer and guess[i] != answer[i]:
            words = list(filter(lambda word: word[i] in answer and word[i] != answer[i] , words))
            print(guess[i], 'is yellow')
            allowed.append(guess[i])
    print(f'There are {len(words)} words left')
    guesses = guesses[1:]
        # else:
        #     words = list(filter(lambda word: guess[i] not in word, words))
    return wordle(guesses, answer, words=words, allowed=allowed)

print(wordle(sys.argv, 'severe'))
