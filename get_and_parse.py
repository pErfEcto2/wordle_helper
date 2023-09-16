from requests import get
from bs4 import BeautifulSoup

url = "https://ru.wiktionary.org"
next_page = "/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0_%D0%B8%D0%B7_5_%D0%B1%D1%83%D0%BA%D0%B2/ru"
c = 0

file = open("words.txt", "a")

while c < 18726:
    print(f"{int(c / 18726 * 100)}%")
    data = BeautifulSoup(get(url + next_page).content, "html.parser")

    l = data.find_all("li")
    l = [i.find("a").attrs.get("title") for i in l if i.find("a")]
    l = l[:200]
    c += len(l)

    l = list(filter(lambda x: x and len(x) == 5, l))
    l = list(map(lambda x: x.lower(), set(l)))

    for i in l:
        file.write(i + "\n")

    next_page = data.find("div", {"id": "mw-pages"}).find_all("a")[-1].attrs.get("href")

file.close()
