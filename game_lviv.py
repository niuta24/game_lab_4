"""
This is the main file for the game. It contains the main loop and the game logic.
"""
class Street:
    """
    A street in the game.
    """
    def __init__(self, street_name):
        """Initialize the street with the given name."""
        self.name = street_name
        self.description = None
        self.linked_streets = {}
        self.character = None
        self.item = None
    def set_description(self, street_description):
        """Set the description of the street."""
        self.description = street_description
    def link_street(self, street_to_link, direction):
        """Link this street to another street in the given direction."""
        self.linked_streets[direction] = street_to_link
    def set_character(self, character):
        """Set the character of the street."""
        self.character = character
    def set_item(self, item):
        """Set the item of the street."""
        self.item = item
    def get_item(self):
        """Return the item of the street."""
        return self.item
    def get_character(self):
        """Return the character of the street."""
        return self.character
    def get_details(self):
        """Print the details of the street."""
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, street in self.linked_streets.items(): 
            print(street.name + " знаходиться у цьому напрямку:" + direction)
    def move(self, direction):
        """Move to the street linked in the given direction."""
        if direction in self.linked_streets:
            return self.linked_streets[direction]
        else:
            print("Тобі туди не можна! Хіба ти хочеш потрапити у Рясне?")
            return self
class Character:
    """
    A character in the game.
    """
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
class Enemy(Character):
    """
    A character in the game.
    """
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.defeated = 0
    def set_conversation(self, conversation):
        """Set what the character will say when talked to."""
        self.conversation = conversation
    def set_weakness(self, item_weakness):
        """Set the weakness of the character."""
        self.weakness = item_weakness
    def describe(self):
        """Print the description of the character."""
        print(self.name + " тут!")
        print(self.description)
    def talk(self):
        """Print the conversation of the character."""
        if self.conversation is not None:
            print("[" + self.name + " говорить]: " + self.conversation)
        else:
            print(self.name + " не хоче говорити з тобою!")
    def fight(self, combat_item):
        """Fight with the character."""
        if combat_item == self.weakness:
            print("Ти переміг " + self.name + " завдяки " + combat_item)
            return True
        else:
            print(self.name + " побив тебе і забрав " + combat_item)
            return False
class Item:
    """A game item."""
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.item = None
    def set_description(self, item_description):
        """Set the description of the item."""
        self.description = item_description
    def set_item(self, item):
        """Set the item of the street."""
        self.item = item
    def describe(self):
        """Print the description of the item."""
        print("Предмет: " + self.name)
        print(self.description)
    def get_name(self):
        """Return the name of the item."""
        return self.name
class Mate:
    pass