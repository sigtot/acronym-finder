#!/usr/bin/env python3
import fileinput


def sorted_string(s: str) -> str:
    return "".join(sorted(s))


# We define a dictionary containing lists of acronyms with their
# common sorted word as the key.
acronym_dict = {}
try:
    for line in fileinput.input(mode="r"):
        word = line.rstrip()  # Removes both \r and \n
        word_key = sorted_string(word)
        if acronym_dict.get(word_key) is None:
            acronym_dict[word_key] = [word]
        else:
            acronym_dict[word_key].append(word)
except FileNotFoundError:
    exit("No such file")


for acronyms in acronym_dict.values():
    if len(acronyms) > 1:
        print(", ".join(acronyms))
