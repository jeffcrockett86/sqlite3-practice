import random
import sys


f = open('wordleAlpha.txt', 'r')
words = f.read().split('\n')[:-1]
answer = words[random.randint(0, len(words))]
# answer = 'memes'
print('Answer is', answer, '\n\n')


def wordle(guesses, answer, words=words, allowed=[], word_length=5):
    if len(guesses) > 0:
        guess = guesses[0]
        print('Guess is', guess)
    if len(guesses)==0:
        return 'That\'s all folks'
    for i in range(word_length):
        if guess[i] == answer[i]:
            words = list(filter(lambda word: word[i] == answer[i] , words))
            allowed.append(guess[i])
            print(guess[i], 'is green')
        if guess[i] in answer and guess[i] != answer[i]:
            words = list(filter(lambda word: word[i] in answer and word[i] != answer[i] , words))
            print(guess[i], 'is yellow')
            allowed.append(guess[i])
        if guess[i] not in answer:
                words = list(filter(lambda word: guess[i] not in word, words))
    if len(words) > 0:
        print(f'\nThere are {len(words)} words left\n')
    guesses = guesses[1:]
    return wordle(guesses, answer, words=words, allowed=allowed)

print(wordle(sys.argv[1:], answer))
