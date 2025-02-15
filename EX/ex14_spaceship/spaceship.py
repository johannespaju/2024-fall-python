"""Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """Initialize crewmate."""
        self.color = color.capitalize()
        self.role = role.title() if role.title() in ["Crewmate", "Sheriff", "Guardian Angel", "Altruist"] else "Crewmate"
        self.tasks = tasks
        self.protected = False

    def __repr__(self):
        """Represent crewmate."""
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Complete task."""
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    """Impostor class."""

    def __init__(self, color: str):
        """Initialize impostor."""
        self.color = color.capitalize()
        self.kills = 0

    def __repr__(self):
        """Represent impostor."""
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        """Initialize spaceship."""
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        """Get crewmate list."""
        return self.crewmate_list

    def get_impostor_list(self):
        """Get impostor list."""
        return self.impostor_list

    def get_dead_players(self):
        """Get dead players."""
        return self.dead_players

    def add_crewmate(self, crewmate: Crewmate):
        """Add crewmate."""
        if crewmate.color not in [player.color for player in self.crewmate_list + self.impostor_list] and isinstance(crewmate, Crewmate):
            self.crewmate_list.append(crewmate)

    def add_impostor(self, impostor: Impostor):
        """Add impostor."""
        if impostor.color not in [player.color for player in self.crewmate_list + self.impostor_list] and len(self.impostor_list) < 3 and isinstance(impostor, Impostor):
            self.impostor_list.append(impostor)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """Kill impostor."""
        if sheriff.role == "Sheriff" and sheriff in self.crewmate_list:
            for impostor in self.impostor_list:
                if impostor.color == color.capitalize():
                    self.impostor_list.remove(impostor)
                    self.dead_players.append(impostor)
                    return

            if sheriff in self.crewmate_list:
                self.crewmate_list.remove(sheriff)
                self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Revive crewmate."""
        if isinstance(dead_crewmate, Crewmate) and dead_crewmate in self.dead_players and altruist.role == "Altruist" and altruist in self.crewmate_list:
            self.crewmate_list.remove(altruist)
            self.dead_players.append(altruist)
            self.dead_players.remove(dead_crewmate)
            self.crewmate_list.append(dead_crewmate)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Protect crewmate."""
        is_someone_already_protected = False
        if guardian_angel.role == "Guardian Angel" and guardian_angel in self.dead_players and crewmate_to_protect in self.crewmate_list:
            for crewmate in self.crewmate_list:
                if crewmate.protected:
                    is_someone_already_protected = True
            if not is_someone_already_protected:
                crewmate_to_protect.protected = True

    def kill_crewmate(self, impostor: Impostor, color: str):
        """Kill crewmate."""
        if impostor in self.impostor_list and impostor.color != color.capitalize():
            for crewmate in self.crewmate_list:
                if crewmate.color == color.capitalize():
                    if crewmate.protected:
                        crewmate.protected = False
                        return
                    self.crewmate_list.remove(crewmate)
                    self.dead_players.append(crewmate)
                    impostor.kills += 1
                    return

    def sort_crewmates_by_tasks(self):
        """Sort crewmates by tasks."""
        return sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)

    def sort_impostors_by_kills(self):
        """Sort impostor by kills."""
        return sorted(self.impostor_list, key=lambda impostor: impostor.kills, reverse=True)

    def get_regular_crewmates(self):
        """Get regular crewmates."""
        return [crewmate for crewmate in self.crewmate_list if crewmate.role == "Crewmate"]

    def get_role_of_player(self, color: str):
        """Get player role."""
        for crewmate in self.crewmate_list:
            if crewmate.color == color.capitalize():
                return crewmate.role
        for impostor in self.impostor_list:
            if impostor.color == color.capitalize():
                return "Impostor"

    def get_crewmate_with_most_tasks_done(self):
        """Get crewmate with most tasks done."""
        return min(self.crewmate_list, key=lambda crewmate: crewmate.tasks)

    def get_impostor_with_most_kills(self):
        """Get impostor with most kills."""
        return max(self.impostor_list, key=lambda impostor: impostor.kills)


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> [Impostor Orange, kills: 0., Impostor Black, kills: 0., Impostor Purple, kills: 0.]
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> [Yellow, role: Guardian Angel, tasks left: 4.]
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    #  spaceship.kill_crewmate(purple, "blue")
    #  print(spaceship.sort_crewmates_by_tasks())  # -> [Red, role: Crewmate, tasks left: 9., White, role: Crewmate, tasks left: 10.]
    #  print(spaceship.sort_impostors_by_kills())  # -> [Impostor Purple, kills: 2., Impostor Orange, kills: 1., Impostor Black, kills: 0.]
    #  print(spaceship.get_regular_crewmates())  # -> [White, role: Crewmate, tasks left: 10., Red, role: Crewmate, tasks left: 9.]
