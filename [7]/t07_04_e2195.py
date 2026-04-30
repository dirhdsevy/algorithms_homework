import sys
import re

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    try:
        first_line = data[0].split()
        n = int(first_line[0])
        m = int(first_line[1])
    except (IndexError, ValueError):
        return

    dictionary = set()
    for i in range(1, n + 1):
        dictionary.add(data[i].strip().lower())

    essay_text = " ".join(data[n+1:n+1+m]).lower()
    essay_words = set(re.findall(r"[a-z]+", essay_text))

    is_subset = essay_words.issubset(dictionary)
    contains_all = dictionary.issubset(essay_words)

    if not is_subset:
        print("Some words from the text are unknown.")
    elif not contains_all:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")

if __name__ == "__main__":
    solve()