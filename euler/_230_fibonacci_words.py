"""
execution:
python euler/_230_fibonacci_words.py 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196

output:
850481152593119296
Duration: 0.000453948974609375s
"""

def fib_until(cutoff, n0=0, n1=1):
    """
    >>> fib_until(20, 0, 1)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    seq = [n0, n1]
    while True:
        if n1 >= cutoff:
            return seq
        n0, n1 = n1, n0+n1
        seq.append(n1)

def char_at_index(D, w0, w1):
    """
    >>> char_at_index(35, "1415926535", "8979323846")
    '9'

    >>> char_at_index(20.5, "dog", "house")
    Traceback (most recent call last):
        ...
    TypeError: The char index must be a positive integer.

    >>> char_at_index(-1, "dog", "house")
    Traceback (most recent call last):
        ...
    TypeError: The char index must be a positive integer.
    """
    if not isinstance(D, int) or D < 1:
        raise TypeError('The char index must be a positive integer.')
    if not isinstance(w0, str) or not isinstance(w1, str):
        raise TypeError('The starting terms must be strings.')

    indices = list(reversed(
        fib_until(D, len(w0), len(w1))
    ))
    L = len(indices)

    i = 0
    while i < L-2:
        if D > indices[i+2]:
            D -= indices[i+2]
        else:
            i += 1
        i += 1
    w = w0 if L-1-i == 0 else w1
    return w[D-1]


if __name__ == '__main__':
    import doctest, sys, time
    doctest.testmod()

    start_time = time.time()
    try:
        w0, w1 = sys.argv[1], sys.argv[2]
    except IndexError:
        print("Two strings must be passed to this script.")
        sys.exit()

    s = 0
    for i in range(18):
        s += pow(10, i) * \
        int(char_at_index(
            (127 + 19*i) * pow(7, i), w0, w1
        ))
    print(s)
    print('Duration: {0}s'.format(time.time() - start_time))
