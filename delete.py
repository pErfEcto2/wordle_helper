with open("words.txt", "r") as f:
    words = list(map(lambda x: x.strip(), f.readlines()))

for word in words:
    for lett in word:
        if not (ord("а") <= ord(lett) <= ord("я") or lett == "ё"):
            words.remove(word)
            break

words = list(set(words))

with open("words.txt", "w") as f:
    for word in words:
        f.write(word + "\n")

