"""
This is the main file for the game. It contains the main loop and the game logic.
"""
class Room:
    """
    A room in the game.
    """
    def __init__(self, room_name):
        """Initialize the room with the given name."""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
    def set_description(self, room_description):
        """Set the description of the room."""
        self.description = room_description
    def link_room(self, room_to_link, direction):
        """Link this room to another room in the given direction."""
        self.linked_rooms[direction] = room_to_link
    def set_character(self, character):
        """Set the character of the room."""
        self.character = character
    def set_item(self, item):
        """Set the item of the room."""
        self.item = item
    def get_item(self):
        """Return the item of the room."""
        return self.item
    def get_character(self):
        """Return the character of the room."""
        return self.character
    def get_details(self):
        """Print the details of the room."""
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items(): 
            print("The " + room.name + " is " + direction)
    def move(self, direction):
        """Move to the room linked in the given direction."""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
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
    defeated = 0 
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def set_conversation(self, conversation):
        """Set what the character will say when talked to."""
        self.conversation = conversation
    def set_weakness(self, item_weakness):
        """Set the weakness of the character."""
        self.weakness = item_weakness
    def describe(self):
        """Print the description of the character."""
        print(self.name + " is here!")
        print(self.description)
    def talk(self):
        """Print the conversation of the character."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    def fight(self, combat_item):
        """Fight with the character."""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer!")
            return False
    def get_defeated(self):
        """Return the defeated status of the character."""
        Enemy.defeated += 1
        return Enemy.defeated
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
        """Set the item of the room."""
        self.item = item
    def describe(self):
        """Print the description of the item."""
        print(self.name + " is here!")
        print(self.description)
    def get_name(self):
        """Return the name of the item."""
        return self.name
class Mate:
    pass