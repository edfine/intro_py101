with open('hamlet.txt', 'r') as fham:
    lham = fham.readlines()
lham.sort(reverse=True)
with open('telmah.txt', 'w') as fhamr:
    print(lham, file=fhamr, end='')