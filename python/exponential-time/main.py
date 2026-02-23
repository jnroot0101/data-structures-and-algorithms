def fib(n):
    """
    This function takes an exponential time algorithm and fixes it up so it can run in polynomial time!
    :param n:
    :return:
    """

    if n <= 1:
        return n

    grandparent, parent, current = 0, 1, 0

    for _ in range(0, n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current

    return current

