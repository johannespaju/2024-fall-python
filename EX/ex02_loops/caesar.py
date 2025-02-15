"""Caesar cipher."""


def encode(message: str, shift: int) -> str:
    """Take a string and turn it into a Caesar cipher."""
    result = ""
    # Go through every letter.
    for char in message:
        # Convert to ascii.
        if char.isalpha():
            char_ascii = ord(char)
            encrypted_ascii = char_ascii + (shift % 26)
            if encrypted_ascii > 122:
                encrypted_ascii -= 26
            new_char = chr(encrypted_ascii)
            result += new_char
        # If not alphabet, add to result without changing
        else:
            result += char
    return result
