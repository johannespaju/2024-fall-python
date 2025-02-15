"""Project 2."""
import re


def is_correct_name(ingredient: str) -> bool:
    """Check if ingredient is only lowercase letters."""
    # Kui ingredienti pole, return empty string
    if ingredient == "":
        return False
    status = True
    # Käi characterid läbi, kui pole lowercase letter ss False
    for char in ingredient:
        if not char.islower():
            status = False
    return status


def fix_names(ingredients: list) -> list:
    """Make uppercase letters lowercase and remove special symbols and numbers."""
    # Empty list for return func at end
    new_ingredients = []
    # Käi läbi iga sõna listis
    for word in ingredients:
        word = word.lower()
        new_word = ""  # Loo tühi string mida täita
        for char in word:  # Käi läbi iga char sõnas
            if char.isalpha():  # Kui on alpha ss lisa uute sõnasse
                new_word += char
        if new_word:  # Kui stringi midagi lisati, siis appendi listi new word
            new_ingredients.append(new_word)
    return new_ingredients


def pizza_at_index(pizzas: list, pizza: str) -> str:
    """Find amount of pizza in list, find result pizza at index of that."""
    count = pizzas.count(pizza)

    if count < len(pizzas):
        return pizzas[count]
    else:
        return ""


def format_orders(nr_order: list) -> dict:
    """Format orders in style {5: 'kanapitsa', 1: 'pepperoni', 20: 'mexican'}."""
    result = {}
    for order in nr_order:
        nr, item = order.split("&")

        nr = int(nr)
        item = item.lower()

        result[nr] = item

    return result


def calculate_income(prices: str) -> float:
    """Calculate income from numbers in string."""
    if not prices:
        return 0.0

    pattern = r'\d{2}\.\d{2}'

    match = re.match(pattern, prices)

    if match:
        return float(match.group()) + calculate_income(prices[4:])
    else:
        return calculate_income(prices[1:])


def switch_keys_and_values(pizza_orders: dict) -> dict:
    """Switch keys and values."""
    result = {}

    for pizza, orders in pizza_orders.items():
        for order in orders:
            if order not in result:
                result[order] = []
            result[order].append(pizza)

    return result


def count_ingredients(menu: dict, order: list) -> dict | None:
    """Count number of ingredients in order."""
    result = {}

    for pizza in order:
        if pizza not in menu:
            return {}

        for ingredient in menu[pizza]:
            if ingredient in result:
                result[ingredient] += 1
            else:
                result[ingredient] = 1

    return result


def match_pizzas_with_prices(pizzas: list, prices: list) -> list:
    """Match pizzas with prices."""
    correct_pizzas = []

    for pizza in pizzas:
        if is_correct_name(pizza) and pizza not in correct_pizzas:
            correct_pizzas.append(pizza)

    if len(correct_pizzas) != len(prices):
        return []

    return list(zip(correct_pizzas, prices))


if __name__ == '__main__':
    print("\nis_correct_name:")
    print(is_correct_name("pizza"))
    print(is_correct_name("Pizza"))
    print(is_correct_name(""))

    print("\nfix_names:")
    print(fix_names(["Tomat1", "SUHKR@", "", "PiIM!", "JuSt#", "###"]))
    print(fix_names([" "]))

    print("\nformat_orders:")
    print(format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]))

    print("\ncalculate_income:")
    print(calculate_income("15.03*05.99|)=01.20&.$50.37"))

    print("\nswitch_keys_and_values:")
    print(switch_keys_and_values({"kanapitsa": [1, 5, 3, 4], "juustupitsa": [1, 2], "pepperoni": [1, 5, 3]}))

    print("\ncount_ingredients:")

    print(count_ingredients({"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]}, ["margarita", "margarita", "pepperoni"]))

    print("\nmatch_pizzas_with_prices:")
    print(match_pizzas_with_prices(["pepperoni", "margarita", "ch7eese", "cheese", "margarita"], [3.99, 4.99, 3.99]))
