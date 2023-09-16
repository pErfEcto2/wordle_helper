def cont_all(sett, strr) -> bool:
    return all([c in strr for c in sett])

def cont_any(sett, strr) -> bool:
    return any([c in strr for c in sett])


with open("words.txt", "r") as f:
    words = list(map(lambda x: x.strip(), f.readlines()))

print("""буквы, которых нет или которые не на своих местах, вводи без пробелов
буквы на своих местах вводи через пробел так: <номер позиции, начиная с 1><буква>
слова для старта: сенат и ролик""")

while True:
    print(f"\nвозможных слов осталось: {len(words)}")
    exclude = list(input("буквы, которых нет: ").strip())
    include = list(input("буквы не на своих местах: ").strip())
    word = input("буквы на своих местах: ").split(" ")

    for w in words.copy():
        if not (cont_all(include, w) and not cont_any(exclude, w)):
            words.remove(w)
            continue
        elif not any(word):
            continue

        for letter in word:
            if w[int(letter[0]) - 1] != letter[1]:
                words.remove(w)
                break

    if len(words) == 0:
        print("у меня закончились слова")
        break
    elif len(words) <= 3:
        print(f"\nосталось только:\n{' '.join(words)}\n")
        break
    print(f"\nпопробуй что-то из этого:\n{' '.join(words[:3])}\n")

