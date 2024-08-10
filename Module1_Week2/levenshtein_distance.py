def levenshtein_distance (token1 , token2):
    if type(token1) != str or type(token2) != str :
        print('Hãy nhập lại 2 chữ cái')

    if token1 == '':
        return len(token1)
    if token2 == '':
        return len(token2)

    token1 = token1.lower()
    token2 = token2.lower()

    n = len(token1)
    m = len(token2)

    lev = [[0 for i in range(m + 1)] for j in range(m + 1)]

    for i in range(n+1) :
        lev[i][0] = i

    for j in range(m+1) :
        lev[0][j] = j

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            del_cost = lev[i-1][j] + 1
            ins_cost = lev[i][j-1] + 1
            sub_cost = lev[i-1][j-1] + (1 if token1[i-1]!= token2[j-1] else 0)
            lev[i][j] = min(del_cost , ins_cost , sub_cost)

    distance = lev[n][m]
    return distance

print(levenshtein_distance ("hola", "hello"))
