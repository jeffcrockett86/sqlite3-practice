import random
import sys

def wordle(guesses, answer, num=5, words=words, allowed=[]):
    guess = guesses[0]
    if len(guess)==0:
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
        # else:
        #     words = list(filter(lambda word: guess[i] not in word, words))
    return wordle(answer, guess=guess[1:][0], words=words, allowed=allowed)

print(wordle(sys.argv))
