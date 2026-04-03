def rm_common(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c = a[i]
                a.remove(c)
                b.remove(c)
                return [a + ["*"] + b, True]
    return [a + ["*"] + b, False]

if __name__ == "__main__":
    n1 = list(input("Player 1 name: ").lower().replace(" ", ""))
    n2 = list(input("Player 2 name: ").lower().replace(" ", ""))

    cont = True
    while cont:
        tmp = rm_common(n1, n2)
        lst, cont = tmp[0], tmp[1]

        idx = lst.index("*")
        n1 = lst[:idx]
        n2 = lst[idx+1:]

    cnt = len(n1) + len(n2)
    res = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    while len(res) > 1:
        sidx = (cnt % len(res)) - 1
        if sidx >= 0:
            res = res[sidx+1:] + res[:sidx]
        else:
            res = res[:len(res)-1]

    print("Relationship status:", res[0])