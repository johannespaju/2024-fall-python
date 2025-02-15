"""Prime number identifier."""


def is_prime_number(number: int) -> bool:
    """Find prime numbers."""
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
