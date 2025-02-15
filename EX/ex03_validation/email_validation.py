"""Email validation."""


def find_domain(email: str):
    """Find if domain is a valid email address."""
    domain = email.split('@')[-1]
    return domain


def has_at_symbol(email: str):
    """Find if email address has @ symbol."""
    if "@" in email:
        return True
    else:
        return False


def is_valid_username(email: str):
    """Find if username is valid."""
    if email.count("@") > 1:
        return False
    username = email.split('@')[0]
    for character in username:
        if not (character.isalnum() or character == '.'):
            return False
    return True


def is_valid_domain(email: str):
    """Find if domain is valid."""
    domain = email.split('@')[-1]
    if email.count("@") > 1:
        return False
    domain_before_period = domain.split(".")[0]
    domain_after_period = domain.split(".")[1]
    if not domain.count(".") == 1:
        return False
    for char in domain:
        if not (char == "." or char.isalpha()):
            return False
    if not (3 <= len(domain_before_period) <= 10):
        return False
    if not (2 <= len(domain_after_period) <= 5):
        return False
    return True


def is_valid_email_address(email: str):
    """Find if email address is valid."""
    if has_at_symbol(email) and is_valid_username(email) and is_valid_domain(email) and email.count("@") < 2:
        return True
    else:
        return False


def create_email_address(domain: str, username: str):
    """Create email address."""
    if not is_valid_username(username):
        return "Cannot create a valid email address using the given parameters!"
    if not is_valid_domain(domain):
        return "Cannot create a valid email address using the given parameters!"
    if domain.count("@") >= 1:
        return "Cannot create a valid email address using the given parameters!"
    if username.count("@") >= 1:
        return "Cannot create a valid email address using the given parameters!"
    return f"{username}@{domain}"


print("Email has the @ symbol:")
print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
print(has_at_symbol("joonas.kivigmail.cosm"))  # -> False

print("\nUsername has no special symbols:")
print(is_valid_username("martalumi@taltech.ee"))  # -> True
print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
print(is_valid_username("marta lumi@taltech.ee"))  # -> False
print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

print("\nFind the email domain name:")
print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
print(find_domain("karlakaru@yahoo.com"))  # -> yahoo.com
print(find_domain("dsasda@autod.ee"))

print("\nCheck if the domain is correct:")
print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
print(is_valid_domain("pannkook@m.oos"))  # -> False
print(is_valid_domain("pannkook@dsas@dsada.com"))

print("\nIs the email valid:")
print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

print("\nCreate your own email address:")
print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
print(create_email_address("koobas.com", "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!
print(create_email_address("france.bise", "ohlala"))
