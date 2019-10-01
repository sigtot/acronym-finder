#!/usr/bin/env python3

import fileinput

words = {}


def sorted_string(s: str) -> str:
    return "".join(sorted(s))


for line in fileinput.input():
    word = line.rstrip()
    word_key = sorted_string(word)
    if words.get(word_key) is None:
        words[word_key] = [word]
    else:
        words[word_key].append(word)

for acronyms in words.values():
    if len(acronyms) > 1:
        print(", ".join(acronyms))
