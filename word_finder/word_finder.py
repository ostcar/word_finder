#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys


def reorder_word(word):
    """
    Returns the word with all letters in alphabetic order.
    """
    return "".join(sorted(list(word)))


def load_wordlist(wordlist_path):
    """
    Returns a dictonary. The keys are the words from the wordlist, but the letters
    in the words are in alphabetic order. The value from any entry is a list with
    all the words which can be build from the key.
    """
    wordlist = {}
    for line in file(wordlist_path):
        word = line.strip()
        reordered_word = reorder_word(word)
        if not reordered_word in wordlist:
            wordlist[reordered_word] = [word]
        else:
            wordlist[reordered_word].append(word)
    return wordlist


def word_in_letters(word, letters):
    """
    Returns True, if the word can be build from the letters.
    The letters from 'word' and 'letters' have to be in alphabetc order.
    """
    word_pointer = 0
    letters_pointer = 0
    while True:
        try:
            word_char = word[word_pointer]
        except IndexError:
            # Wenn das Wort zuende ist, dann passt es in chars
            return True
        try:
            letters_char = letters[letters_pointer]
        except IndexError:
            # Wenn chars zuende sind, passt das wort nicht rein
            return False

        if word_char == letters_char:
            # Wenn die Buchstaben übereinstimmen, dann fahre fort
            word_pointer += 1
        letters_pointer += 1


def filter_wordlist(wordlist, letters):
    """
    Returns a wordlist in which any word can be build from letters.
    Wordlist has to be dictonary with alphabetic ordered words as keys.
    """
    filtered_wordlist = {}
    ordered_letters = reorder_word(letters)
    for key in wordlist:
        if word_in_letters(key, ordered_letters):
            filtered_wordlist[key] = wordlist[key]
    return filtered_wordlist


def score_word(word, letters, letters_score):
    """
    Builds a score for the word.
    'letters' and letters_score has to be a list with 3 entries.
    """
    # TODO: only use letters in each group one time.
    score = 0
    for letter in word:
        for i in range(2):
            if letter in letters[i]:
                score += letters_score[i]
    return score


def score_wordlist(wordlist, letters, letters_score=[5, 1, 0]):
    """
    Build a score for any word in the wordlist.
    'wordlist' has to be an wordlist-dict. See load_wordlist.
    Returns a list from 2-entry-tubles. The first entry is the score, and the
    second are any words which can be build from the word.
    """
    scored_wordlist = []
    for key in wordlist:
        score = score_word(key, letters, letters_score)
        scored_wordlist.append((score, wordlist[key]))
    return scored_wordlist


def sort_scored_wordlist(scored_wordlist):
    """
    Return a sorted version from a scored wordlist.
    """
    return sorted(scored_wordlist, key=lambda a: a[0], reverse=True)


def print_scored_wordlist(scored_wordlist):
    for item in scored_wordlist:
        print item[0], " ".join(item[1])


def get_words(letters, count=10, wordlist_path=None):
    if wordlist_path is None:
        wordlist_path = os.path.join(os.path.dirname(__file__), 'wordlist-en.txt')
    all_letters = letters['own'] + letters['neutral'] + letters['other']
    wordlist = load_wordlist(wordlist_path)
    wordlist = filter_wordlist(wordlist, all_letters)
    scored_wordlist = score_wordlist(wordlist, [letters['other'],
                                                letters['neutral'],
                                                letters['own']])
    words = []
    for element in sort_scored_wordlist(scored_wordlist):
        for word in element[1]:
            words.append(word)
        if len(words) >= count:
            break
    return words[:count]


def main(argv):
    own_letters = argv[0]
    neutral_letters = argv[1]
    opponent_letters = argv[2]
    try:
        wordlist_path = argv[3]
    except IndexError:
        wordlist_path = 'wordlist-en.txt'

    letters = own_letters + neutral_letters + opponent_letters
    wordlist = load_wordlist(wordlist_path)
    wordlist = filter_wordlist(wordlist, letters)
    scored_wordlist = score_wordlist(wordlist, [opponent_letters, neutral_letters, own_letters])
    print_scored_wordlist(sort_scored_wordlist(scored_wordlist))
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])

