"""Phone numbers."""


def add_country_code(number: str) -> str:
    """
    Return number with country code.

    The input string contains a phone number. If the phone number doesn't have a country code, add one
    """
    if "+" in number:
        return number
    else:
        return "+372 " + number


def is_valid(number: str) -> bool:
    """
    Check if phone number is valid.

    The input string contains a phone number. Check if the number is valid:
    Number is correct when it has a country code, a "+" before it, other numbers (at least 7) and
    it doesn't have any special characters or letters
    """
    if not number.count(" ") == 1:
        return False
    country_code = number.split(" ", 1)[0]
    phone_number = number.split(" ", 1)[1]

    if not (country_code.count("+") == 1 and country_code.startswith("+") and country_code[1:].isnumeric()):
        return False
    if not phone_number.isnumeric():
        return False
    if len(phone_number) < 7:
        return False
    return True


def remove_unnecessary_chars(number: str) -> str:
    """Remove unnecessary characters from phone number."""
    country_code = number.split(" ", 1)[0]

    def is_country_code_valid(country_code) -> bool:
        """Check if country code is valid."""
        country_code = number.split(" ", 1)[0]
        return number.startswith("+") and any(char.isnumeric() for char in country_code) and " " in number

    has_country_code = is_country_code_valid(country_code)

    new_number = ""
    number_of_plus = 0
    number_of_space = 0

    if has_country_code:
        for char in number:
            if number_of_plus == 0:
                new_number += char
                number_of_plus += 1
            elif char.isnumeric():
                new_number += char
            elif char == " " and number_of_space == 0:
                number_of_space += 1
                new_number += char

    else:
        for char in number:
            if char.isnumeric():
                new_number += char

    return new_number


def get_last_numbers(numbers: list[str], n: int) -> list[str]:
    """Get last n numbers."""
    if n <= 0:
        return []

    elif n > len(numbers):
        return numbers

    else:
        return numbers[-n:]


def get_first_correct_number(names: list[str], numbers: list[str], name: str) -> str | None:
    """Get first correct number."""
    name = name.lower()

    for i, current_name in enumerate(names):
        if current_name.lower() == name.lower():
            phone_number = numbers[i]
            if is_valid(phone_number):
                return phone_number

    return None


def correct_numbers(numbers: list[str]) -> list[str]:
    """Take in numbers and return only correct numbers."""
    new_list = []

    for number in numbers:
        if is_valid(number):
            new_list.append(number)
        elif not is_valid(number):
            number = remove_unnecessary_chars(number)
            number = add_country_code(number)
            if is_valid(number):
                new_list.append(number)

    return new_list


def get_names_of_contacts_with_correct_numbers(names: list[str], numbers: list[str]) -> list[str]:
    """Get names of contacts with correct numbers."""
    valid_names = []

    def name_formatted(name: str) -> str:
        parts = name.split(" ")
        return f"{parts[0].capitalize()} {parts[1].capitalize()}"

    for i in range(len(names)):
        name = names[i]
        number = numbers[i]
        if is_valid(number):
            valid_names.append(name_formatted(name))

    return valid_names
