"""Password validation."""
import math


def is_correct_length(password: str) -> bool:
    """
    Check if the password's length is within the valid range.

    The password should have a length between 8 and 64 symbols.
    :param password: Password to be checked
    :return: True if the password's length is within the valid range, False otherwise.
    """
    if 8 <= len(password) <= 64:
        return True
    else:
        return False


def includes_uppercase(password: str) -> bool:
    """
    Check if the password contains at least one uppercase letter.

    :param password: Password to be checked
    :return: True if the password contains at least one uppercase letter, False otherwise.
    """
    for uppercase in password:
        if uppercase.isupper():
            return True
    return False


def includes_lowercase(password: str) -> bool:
    """
    Check if the password contains at least one lowercase letter.

    :param password: Password to be checked
    :return: True if the password contains at least one lowercase letter, False otherwise.
    """
    for lowercase in password:
        if lowercase.islower():
            return True
    return False


def includes_special(password: str) -> bool:
    """
    Check if the password contains at least one special character (whitespace is also considered a special character).

    :param password: Password to be checked
    :return: True if the password contains at least one special character, False otherwise.
    """
    for special in password:
        if not special.isalnum():
            return True
    return False


def includes_number(password: str) -> bool:
    """
    Check if the password contains at least one numeric digit.

    :param password: Password to be checked
    :return: True if the password contains at least one numeric digit, False otherwise.
    """
    for number in password:
        if number.isdigit():
            return True
    return False


def is_different_from_old_password(old_pass: str, new_pass: str) -> bool:
    """
    Check if the new password is different enough from the old password.

    The overlap between the new password and old password should be less than 50%.
    The check for overlap is case-insensitive.
    The overlap is also checked for the reversed version of the new password.

    :param old_pass: The old password
    :param new_pass: The new password
    :return: True if the new password is different enough, False otherwise.
    """
    old_pass = old_pass.lower()  # Convert to lowercase
    new_pass = new_pass.lower()  # Convert to lowercase
    reversed_old_pass = old_pass[::-1]
    half = math.ceil(len(new_pass) / 2)
    for i in range(len(new_pass) - half + 1):
        subword = new_pass[i:i + half]
        if subword in old_pass or subword in reversed_old_pass:
            return False
    return True


def is_name_in_password(password: str, name: str) -> bool:
    """
    Check if the password contains the name of the account owner.

    The name received as input may contain whitespace to separate the first and last name, neither of which should be
    present in the password.
    If the name contains a hyphen (such as Mari-Liis), neither part of the name should be present in the password.
    The name should not be in the password even if the casing of it is different in the password.
    Reversed format of the name is also not allowed in the password

    :param password: The password to be validated
    :param name: The full name of the account owner
    :return: True if the name is present in the password, False otherwise.
    """
    password = password.lower()
    name = name.lower()
    name_without_hyphen = name.replace('-', ' ').split()
    for matching in name_without_hyphen:
        matching = matching.lower()
        if matching in password or matching[::-1] in password:
            return True
    return False


def is_birthday_in_password(password: str, birthdate: str) -> bool:
    """
    Check if the password contains the birthday of the account owner.

    The day, month or year in the birthdate cannot be present in the password. For the birth year, the last two digits
    of the birth year separately is also not allowed.

    For the day, month or last 2 digits of the year, the reversed number is allowed but for the full 4-digit year is
    not allowed in the reverse format.

    The date is always in the format "dd.mm.yyyy", where
    dd is 2-digit day (01, 02, .. 31)
    mm is 2-digit month (01, 02, .. 12)
    yyyy is 4-digit year (0001, 0002, ..., 2022, 2023, ..., 3000, ...)

    You don't have to validate the date.

    :param password: The password to be validated
    :param birthdate: Birthday of the account owner, format is dd.mm.yyyy
    :return: True if the birthday is present in the password, False otherwise
    """
    birth_days = birthdate[0:2]
    birth_months = birthdate[3:5]
    birth_years = birthdate[6:10]
    birth_years_last_two = birth_years[2:4]

    reverse_birth_days = birth_days[::-1]
    reverse_birth_months = birth_months[::-1]
    reverse_birth_years_last_two = birth_years_last_two[::-1]

    if birth_days in password or birth_months in password or birth_years in password or birth_years_last_two in password:
        return True

    if reverse_birth_days in password or reverse_birth_months in password or reverse_birth_years_last_two in password:
        return False
    else:
        return False


def is_password_valid(new_password: str, old_password: str, name: str, birthdate: str) -> bool:
    """
    Check whether the given password is valid.

    This function combines several checks to determine if the provided password is valid.
    It checks the length, presence of uppercase and lowercase letters, inclusion of at least one number,
    inclusion of at least one special character, absence of the user's name and birthdate in the password.
    Call the functions you wrote before within this one to complete the validation.

    :param new_password: The password to be checked
    :param old_password: the previous password of this account
    :param name: The user's full name
    :param birthdate: The user's birthdate
    :return: True if the password is valid, False otherwise.
    """
    if is_correct_length(new_password) and includes_uppercase(new_password) and includes_lowercase(new_password) and includes_special(new_password) and includes_number(new_password) and is_different_from_old_password(old_password, new_password) and not is_name_in_password(new_password, name) and not is_birthday_in_password(new_password, birthdate):
        return True
    else:
        return False
