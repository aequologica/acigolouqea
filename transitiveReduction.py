# cf. Michael Clerx answer @ http://stackoverflow.com/questions/1690953/transitive-reduction-algorithm-pseudocode

def prima(m, title=None):
    """ Prints a matrix to the terminal """
    if title:
        print(title)
    for row in m:
        print(', '.join([str(x) for x in row]))
    print ('')

def path(m):
    """ Returns a path matrix """
    p = [list(row) for row in m]
    n = len(p)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            if p[j][i]:
                for k in range(0, n):
                    if p[j][k] == 0:
                        p[j][k] = p[i][k]
    return p

def hsu(m):
    """ Transforms a given directed acyclic graph into its minimal equivalent """
    n = len(m)
    for j in range(n):
        for i in range(n):
            if m[i][j]:
                for k in range(n):
                    if m[j][k]:
                        m[i][k] = 0

m = [   [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]]

prima(m, 'Original matrix')
hsu(m)
prima(m, 'After Hsu')

p = path(m)
prima(p, 'Path matrix')
hsu(p)
prima(p, 'After Hsu')