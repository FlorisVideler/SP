def move(n, ch=1011000):
    lst = list(map(int, str(ch)))  # Maak list van ch zodat het makkelijker is om getallen te verplaatsen
    tmplst, addlst = lst[n:], lst[:n]
    for i in addlst:
        tmplst.append(i)
    nch = int(''.join(map(str, tmplst)))
    return nch


print(move(3))
