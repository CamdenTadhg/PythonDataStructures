def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    potential = 1
    value = num
    factor1 = []
    factor2 = []
    while potential < value:
        if num % potential == 0:
            factor1.append(potential)
            factor2.append(int(num/potential))
        value = num/potential
        potential = potential + 1
    factor2.reverse()
    factor1.extend(factor2)
    return factor1