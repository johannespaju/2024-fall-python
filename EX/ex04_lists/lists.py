"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).
    """
    if not all_phones:
        return []
    # If empty string, return empty string

    phones = list(all_phones.split(","))
    # Split phones into list, phones are separated by commas

    return phones


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).
    Only include brand, so the first word before " "
    """
    #p = list_of_phones(all_phones)
    if not all_phones:
        return []
    #  If empty string, return empty string

    phones = all_phones.split(",")
    brands = []
    # Split list into phones, phones separated by ","

    for phone in phones:
        brand = phone.split(" ")[0]
        if brand not in brands:
            brands.append(brand)
    # Go through each phone in list, take first word in each phone and add it to list(if not already in it)

    return brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).
    """
    if not all_phones:
        return []

    phones = all_phones.split(",")
    models = []

    for phone in phones:
        model = phone.split(" ", 1)[1]
        if model not in models:
            models.append(model)
    # Go through each phone in list, split phone brand, number combo into two after the first space, add part that's after " "

    return models


def search_by_brand(all_phones: str, brand: str) -> list:
    """
    Search for phones by brand.

    The search is case-insensitive.
    """
    search_results = []
    phones = all_phones.split(",")
    brand = brand.lower()

    for phone in phones:
        phone_brand = phone.split(" ")[0].lower()
        # Take the first word in each phone, convert to lowercase
        if brand == phone_brand:
            search_results.append(phone)
        # If brand searched for is the same as first word in phone name, return whole phone name in original capitalization

    return search_results


def search_by_model(all_phones: str, model: str) -> list:
    """
    Search for phones by model.

    The search is case-insensitive.
    """
    search_results = []
    phones = all_phones.split(",")
    model = model.lower()

    for phone in phones:
        phone_parts = phone.split(" ")
        # Split after each space to get individual words, .split() turns string into list
        model_parts = phone_parts[1:]
        # Give list of every word after the brand name ['12', 'Max']

        lowercased_model_parts = []
        # Empty list to add model parts in lowercase, since cant convert list to lowercase directly
        for word in model_parts:
            lowercased_model_parts.append(word.lower())
        # Add each individual word back to list lowercased [12, max]

        if model in lowercased_model_parts:
            search_results.append(phone)
        # If model matches directly with at least one of model parts, add to phone search_results ['iPhone 12 Max','etc.']

    return search_results


if __name__ == '__main__':
    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))
    # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))
    # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))
    # ['Google']
    print(phone_brands(""))
    # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))
    # ['14', 'Pixel', 'Magic5']
    print(phone_models("IPhone 14 A,Google Pixel B,Honor Magic5,IPhone 14"))
    # ['14 A', 'Pixel B', 'Magic5', '14']
    print(phone_models("LG Optimus Black"))
    # ['Optimus Black']
    print(search_by_brand("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "iphone"))
    # ['IPhone X', 'IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "pro"))
    # ['IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "1"))
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "IPhone"))
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "12 Pro"))
    # []
