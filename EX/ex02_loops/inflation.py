"""Inflation."""


def inflation(n: int, goal: int) -> int:
    """Increase the given positive number until it reaches the goal (or goes over it)."""
    while n < goal:
        if goal / n == 2:
            n = n * 2
        elif n < 10:
            n = n * 5
        elif 10 <= n < 100:
            n = n * 4
        elif 100 <= n < 1000:
            n = n * 3
        elif 1000 <= n < 10000:
            n = n * 2
        else:
            n = n * 7
    return n
