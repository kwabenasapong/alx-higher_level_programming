#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    items = dir(hidden_4)

    for i in range(len(items)):
        word = items[i]
        if word[0] != '_':
            print(word)
