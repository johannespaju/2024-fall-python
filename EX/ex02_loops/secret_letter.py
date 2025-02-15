"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """Check if the given secret letter follows all the necessary rules. Return True if it does, else False."""
    count_upper = 0
    count_lower = 0
    count_sum_of_numbers = 0
    for letters in letter:
        if letters.isupper():
            count_upper += 1
        if letters.islower():
            count_lower += 1
        if letters.isdigit():
            count_sum_of_numbers += int(letters)
    if count_upper > count_lower and count_sum_of_numbers <= count_upper and count_sum_of_numbers >= count_lower:
        return True
    else:
        return False
