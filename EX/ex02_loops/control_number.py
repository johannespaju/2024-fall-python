"""Control number."""


def control_number(encrypted_string: str) -> bool:
    """Given encrypted string that has a control number in the end of it, return True if correct, else False."""
    count_control_number = 0
    count_last_digits = ""
    special_symbol = "?!#@"
    for i in encrypted_string:
        if i.islower():
            count_control_number += 1
        if i.isupper():
            count_control_number += 2
        if i in special_symbol:
            count_control_number += 5
    for last_digits in reversed(encrypted_string):
        count_last_digits = last_digits + count_last_digits
    if count_last_digits.endswith(str(count_control_number)):
        return True
    return False
