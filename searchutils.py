from bs4 import BeautifulSoup

def get_inn(dom, rt):
    inn = "0"
    adr = 'https://www.reg.ru/whois/' + dom
    re = rt.get(adr)
    soup = BeautifulSoup(re.text, "html.parser")
    quotes = soup.find_all('div', class_='ds-table__cell-content')
    spis = []
    for ele in quotes:
        s = ''.join(ele.text.split())
        if len(s) > 1:
            spis.append(s)
    i = 0
    for x in spis:
        if x == "ИНН":
            inn = spis[i + 1]
        i = i + 1
    return inn
