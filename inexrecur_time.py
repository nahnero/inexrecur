# Started Wed 25 Mar 00:56:18 2020 by nahnero. #
def script ():
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
    #  for i in IS: print (i)

    # coding: utf-8

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(function, args=tuple(), kwargs={}):
    # https://gist.github.com/turicas/5278558
    '''Return `real`, `sys` and `user` elapsed time, like UNIX's command `time`
    You can calculate the amount of used CPU-time used by your
    function/callable by summing `user` and `sys`. `real` is just like the wall
    clock.
    Note that `sys` and `user`'s resolutions are limited by the resolution of
    the operating system's software clock (check `man 7 time` for more
    details).
    '''
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function(*args, **kwargs)
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return {'real': (end_time - start_time),
            'sys': (end_resources.ru_stime - start_resources.ru_stime),
            'user': (end_resources.ru_utime - start_resources.ru_utime)}


if __name__ == '__main__':
    def test(iterations):
        for i in range(iterations):
            script ()

    its = 10000
    t = unix_time(test, (its, ))
    for i in t:
        print ("%s %.2f"%(i, 1e6*t[i]/its))
