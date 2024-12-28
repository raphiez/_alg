def perm(n):

    def perm_next(n, p):
        if len(p) == n:
            print(p)
            return

        
        for x in range(n):
            if x not in p:
                p.append(x)
                perm_next(n, p)
                p.pop()

    perm_next(n, [])

perm(2)
perm(3)
perm(4)
perm(5)
