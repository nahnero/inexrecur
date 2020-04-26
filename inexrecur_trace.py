# Started Wed 25 Mar 00:56:18 2020 by nahnero. #
def CalculateD (W):
    D = [0]*len (W)
    z, j = 0, 0
    for i in range (len (W)):
        if W[j:i] not in X:
            z += 1
            j = i + 1
        D[i] = z
    return D

def InexRecur (W, i, z, k, l, depth):
    if i < 0:
        if z < 0:
            return set ([])
        else:
            print ('-'*19, '{%d,%d}' % (k, l),'-'*13)
            return set ([(k, l)])
    if z < D[i]:
        return set ([])
    I = set ([])
    print ("%sDeletion\r\t\t     [%s]    %2d %2d %2d %2d" %\
            (' '*depth, W[i], i-1, z-1, k, l))
    I = I.union (InexRecur (W, i-1, z-1, k, l, depth + 1))
    for bi in dic:
        ki = C (bi) + O (bi, k-1) + 1
        li = C (bi) + O (bi, l)
        if ki <= li:
            print ("%sInsertion\r\t\t     [%s]    %2d %2d %2d %2d" %\
                (' '*depth, bi, i, z-1, ki, li))
            I = set (I.union (InexRecur (W, i, z-1, ki, li, depth + 1)))
            if bi == W[i]:
                print ("%sMatch\r\t\t     [%s]    %2d %2d %2d %2d" %\
                    (' '*depth, bi, i-1, z, ki, li))
                I = set (I.union (InexRecur (W, i-1, z, ki, li, depth + 1)))
            else:
                print ("%sSubstitution\r\t\t [%s] -> [%s] %2d %2d %2d %2d" %\
                    (' '*depth, bi, W[i], i-1, z-1, ki, li))
                I = set (I.union (InexRecur (W, i-1, z-1, ki, li, depth  + 1)))
    return I

def InexSearch (W, z):
    print ("\r\t\t  Mutation   i  z  k  l")
    return InexRecur (
            W = W,
            i = len (W)-1,
            z = z,
            k = 1,
            l = len (X)-1,
            depth = 0)
X = 'googol$';
W = 'gool'
dic = ''.join (sorted (set (X.replace ('$', ''))))

BWT  = [[(X*2)[i:i+len (X)], i] for i in range (len (X))]
BWT.sort ()
S, B = [], ''
for i in BWT: S.append (i[1]); B += (i[0][-1])
C = lambda a: ''.join (sorted (X.replace ('$', '')))[0:-2].find (a)
O = lambda a, i: B[0:i+1].count (a)

#  D = CalculateD (W)
D = [0,0,0,1]

IS = InexSearch (W, 1)
#  print (IS)
