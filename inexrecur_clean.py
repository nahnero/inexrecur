#!/usr/bin/env python
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

def InexRecur (W, i, z, k, l):
    if i < 0:
        if z < 0:
            return set ([])
        else:
            return set ([(k, l)])
    if z < D[i]:
        return set ([])
    I = set ([])
    I = I.union (InexRecur (W, i-1, z-1, k, l))
    for bi in dic:
        ki = C (bi) + O (bi, k-1) + 1
        li = C (bi) + O (bi, l)
        if ki <= li:
            I = set (I.union (InexRecur (W, i, z-1, ki, li)))
            if bi == W[i]:
                I = set (I.union (InexRecur (W, i-1, z, ki, li)))
            else:
                I = set (I.union (InexRecur (W, i-1, z-1, ki, li)))
    return I

def InexSearch (W, z):
    return InexRecur (
            W = W,
            i = len (W)-1,
            z = z,
            k = 0,
            l = len (X)-1)
X = 'googol$';
W = 'lol'
dic = ''.join (sorted (set (X.replace ('$', ''))))

BWT  = [[(X*2)[i:i+len (X)], i] for i in range (len (X))]
BWT.sort ()
S, B = [], ''
for i in BWT: S.append (i[1]); B += (i[0][-1])
C = lambda a: ''.join (sorted (X.replace ('$', '')))[0:-2].find (a)
O = lambda a, i: B[0:i+1].count (a)

D = CalculateD (W)

IS = InexSearch (W, 1)
for i in IS: print (i)
