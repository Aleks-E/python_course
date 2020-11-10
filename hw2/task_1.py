"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List

import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    words_unique = {}
    with open(file_path, "r") as data:
        for line in data:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                if word != "":
                    word = word.encode().decode("unicode-escape")
                    word = word.translate(word.maketrans("", "", string.punctuation))
                    if word not in words_unique:
                        words_unique[word] = len(set(word))

        words_list = list(words_unique.items())
        words_list.sort(key=lambda x: x[1], reverse=True)
        longest_unique_words = []
        for i in range(10):
            longest_unique_words.append(words_list[i][0])

        return longest_unique_words


def get_rarest_char(file_path: str) -> str:
    symbols = {}
    with open(file_path, "r") as data:
        for line in data:
            line = line.rstrip()
            line = line.encode().decode("unicode-escape")
            for symbol in line:
                if symbol != " ":
                    if symbol not in symbols:
                        symbols[symbol] = 1
                    else:
                        symbols[symbol] += 1

        symbols_list = list(symbols.items())
        symbols_list.sort(key=lambda x: x[1])
        return symbols_list[0][0]


def count_punctuation_chars(file_path: str) -> int:
    punct_chars_qtt = 0
    with open(file_path, "r") as data:
        for line in data:
            line = line.rstrip()
            line = line.encode().decode("unicode-escape")
            for symbol in line:
                if symbol in string.punctuation:
                    punct_chars_qtt += 1
        return punct_chars_qtt


def count_punctuation_chars_alternative_1(
    file_path: str,
) -> int:
    punct_chars_qtt = 0
    with open(file_path, "r") as data:
        for line in data:
            line = line.rstrip()
            line = line.encode().decode("unicode-escape")
            length_with_punct = len(line)
            line = line.translate(line.maketrans("", "", string.punctuation))
            length_without_punct = len(line)
            punct_chars_qtt = punct_chars_qtt + length_with_punct - length_without_punct
        return punct_chars_qtt


def count_non_ascii_chars(file_path: str) -> int:
    not_ascii_chars_qtt = 0
    with open(file_path, "r") as data:
        for line in data:
            line = line.rstrip()
            line = line.encode().decode("unicode-escape")
            for symbol in line:
                if symbol not in string.printable:
                    not_ascii_chars_qtt += 1
        return not_ascii_chars_qtt


def get_most_common_non_ascii_char(file_path: str) -> str:
    not_ascii_chars = {}
    with open(file_path, "r") as data:
        for line in data:
            line = line.rstrip()
            line = line.encode().decode("unicode-escape")
            for symbol in line:
                if symbol not in string.printable:
                    if symbol not in not_ascii_chars:
                        not_ascii_chars[symbol] = 1
                    else:
                        not_ascii_chars[symbol] += 1
        not_ascii_chars = list(not_ascii_chars.items())
        not_ascii_chars.sort(key=lambda x: x[1])
        return not_ascii_chars[-1][0]
