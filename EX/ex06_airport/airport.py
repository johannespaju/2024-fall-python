"""Airport schedule."""


def destinations_and_times(flights: list) -> dict:
    """
    Create a dictionary containing destinations with the departure times for this destination today.

    Flights in the list are in the format: "Tallinn,08:00,01h30m,OWL1234"
    Where different parts are separated by comma:
    - destination
    - departure time
    - flight duration
    - flight number

    Result format: {destination1: [time1, time2, ...], destination2: [time1, time2, ...]}.

    The order of departure times and destinations are not important.

    :param flights: given list from database.
    :return: dictionary where keys are destinations and values are lists of departure times.
    """
    new_dict = {}
    # Create empty dictionary for return.
    for flight in flights:
        flight_destination = flight.split(',')[0]
        flight_time = flight.split(',')[1]
        # Take destination and departure time from each flight.

        if flight_destination in new_dict:
            new_dict[flight_destination].append(flight_time)
            # If Destination already has a flight, use append to not overwrite it.
        else:
            new_dict[flight_destination] = [flight_time]
            # If destination doesn't have a flight, add destination to dictionary.

    return new_dict


def sort_dict_values(dictionary: dict) -> dict:
    """
    Sort dictionary values in ascending order.

    This function should be applied to the previous function's result to get the departure times ordered.

    Return a dictionary where all the values are in ascending order.
    The order of the keys is not important.
    """
    sorted_dict = {}
    # Create sorted_dict for return at the end.

    for key, value in dictionary.items():
        sorted_dict[key] = sorted(value)
        # Sort flight times in ascending order

    return sorted_dict


def flights_to_destination(flights: list, destination: str) -> list:
    """
    Return flight times for the given destination.

    People want to know when flights for their chosen destination take off today.
    Using the functions written before, find and return the list of departure times
    (in ascending order) for that destination today.

    If there are no flights to the chosen destination, return empty list.

    :param flights: given list from database (the same as in destinations_and_times).
    :param destination: chosen destination for which we want to know the departure times.
    :return: list of departures (sorted in ascending order) for that destination.
    """
    flights_dict = destinations_and_times(flights)  # Create dictionary of flights using first function.

    sorted_flights_dict = sort_dict_values(flights_dict)  # Use second function to sort flights in ascending time

    if destination in sorted_flights_dict:
        return sorted_flights_dict[destination]
    # If searched destination is in the flight plan, use destination as key for searching for flights

    return []
    # If there are no flights to the chosen destination, return empty list.


def flights_schedule(flights: list) -> dict:
    """
    Return flight schedule by departure times.

    Create a dictionary containing the flight schedule for the day, where the keys are the departure times
    and the values are tuples which contain the destination and the flight number
    {time1: (destination, flight_number), time2: (destination, flight_number), ...}.

    The order of the keys (departure times) is not important.

    :param flights: given list from database (the same as in destinations_and_times).
    :return: dictionary where the keys are departure times and values are tuples containing the destination and
    flight number.
    """
    new_dict = {}

    for flight in flights:
        flight_destination = flight.split(',')[0]
        flight_time = flight.split(',')[1]
        flight_number = flight.split(',')[3]
        new_dict[flight_time] = (flight_destination, flight_number)
    # For loop and add each thing to right place

    return new_dict


def destinations_list(schedule: dict) -> list:
    """
    Return a list of unique destinations for the day from the given flight schedule, sorted alphabetically.

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :return: Alphabetically sorted list of unique destinations.
    """
    destinations = set()  # Create empty set for destinations to make sure no duplicates
    for destination, flight_number in schedule.values():  # Go through and add the destination to set
        destinations.add(destination)

    return sorted(list(destinations))  # Make destinations a list and return it sorted


def airlines_operating_today(schedule: dict, airline_names: dict) -> set:
    """
    Return a set of unique airline names that have flights operating today.

    Schedule is the result of the flights_schedule function.
    Airline names are presented as a dictionary where the key is the airline code
    and the value is the corresponding airline name.

    Flight code contains 3 letters and 4 numbers. The 3-letter code indicates the airline code.
    So, the 3-letter code should be taken from the airline_names dictionary (key).

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing airline codes and corresponding names.
    :return: Set of unique airline names operating today.
    """
    operating_airlines = set()  # Create empty set for unique airlines

    for destination, flight_number in schedule.values():
        airline_code = flight_number[:3]  # Airline code the first 3 characters in flight number
        if airline_code in airline_names:  # If airline code in airline_names dictionary ->
            operating_airlines.add(airline_names[airline_code])  # Add airline name from dict to set

    return operating_airlines


def destinations_by_airline(schedule: dict, airline_names: dict) -> dict:
    """
    Return a dictionary of destinations by airline names.

    Returns a dictionary where the keys are airline names and the values are sets of unique destinations
    that the airline is flying to today.

    Airline names is in the same format as in airlines_operating_today.
    The 3-letter code from the flight number can be used to find the airline name.

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing mapping of airline codes to airline names.
    :return: Dictionary of airline names to sets of destinations.
    """
    airline_destinations = {}  # Create empty dict

    for time, (destination, flight_number) in schedule.items():  # Add () to open up tuple for example ({'08:00': ('Tallinn', 'OWL1234'))
        airline_code = flight_number[:3]
        if airline_code in airline_names:
            airline_name = airline_names[airline_code]  # Find airline name using airline_names dictionary
            if airline_name not in airline_destinations:
                airline_destinations[airline_name] = set()  # If airline is not already in dictionary, create new empty set for destinations

            airline_destinations[airline_name].add(destination)  # Add destination to set in dictionary

    return airline_destinations


if __name__ == '__main__':
    flights = [
        "Tallinn,08:00,01h30m,OWL1234",
        "Helsinki,10:35,01h00m,BHM5678",
        "Tallinn,09:00,01h30m,OWL1235",
    ]

    print(destinations_and_times(flights))
    # {'Tallinn': ['08:00', '09:00'], 'Helsinki': ['10:35']}

    flights_dict = {'Tallinn': ['10:00', '09:00'], 'Helsinki': ['10:35']}
    print(sort_dict_values(flights_dict))
    # {'Tallinn': ['09:00', '10:00'], 'Helsinki': ['10:35']}

    print(flights_to_destination(flights, "Tallinn"))
    # ['08:00', '09:00']

    print(flights_schedule(flights))
    # {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}

    schedule = {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}
    print(destinations_list(schedule))
    # ['Helsinki', 'Tallinn']

    airlines = {"OWL": "Owlbear Airlines", "BHM": "Beholder's Majesty Airlines"}

    print(airlines_operating_today(schedule, airlines))
    # {'Owlbear Airlines', "Beholder's Majesty Airlines"}

    print(destinations_by_airline(schedule, airlines))
    # {'Owlbear Airlines': {'Tallinn'}, "Beholder's Majesty Airlines": {'Helsinki'}}