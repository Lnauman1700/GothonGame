

class Map(object):

    def __init__(self, start_room):
        self.start_room = start_room

    def next_scene(self, scene_name):
        # changes the starting room to instead be a new room object. Now, when the engine moves on to call the opening scene again, the opening scene will be new and improved
        self.start_room = scene_name

    def opening_scene(self):
        # should run the starting scene, so call start_room.enter
        val = self.start_room.enter()
        if val == "victory":
            return "victory"
        return "death"

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # When you call this, it should run the scene_map.opening_scene(). This'll start the game
        val = self.scene_map.opening_scene()
        # upon victory, though, we should change some stuff up. we should run the next_scene function with a new scene as a param so that scene can get played.
        # if you lose, well, the death Scene plays.
        if val == "victory":
            self.scene_map.next_scene(LaserWeaponArmory())
        elif val == "death":
            self.scene_map.next_scene(Death())

        val = self.scene_map.opening_scene()
        if val == "victory":
            self.scene_map.next_scene(Bridge())
        elif val == "death":
            self.scene_map.next_scene(Death())

        val = self.scene_map.opening_scene()
        if val == "victory":
            self.scene_map.next_scene(EscapePod())
        elif val == "death":
            self.scene_map.next_scene(Death())

        val = self.scene_map.opening_scene()
        if val == "victory":
            print("You beat the game!")
        elif val == "death":
            self.scene_map.next_scene(Death())





class Scene(object):

    def enter(self):
        pass


class Death(Scene):

    def enter(self):
        print("sorry bud, you died")

class Bridge(Scene):

    def enter(self):
        print("You find yourself in a fight with yet another Gothon! Will you...")
        print("1. Threaten to blow up the ship with a bomb")
        print("2. rely on good ol' fisticuffs")

        choice = input("> ")

        if choice == "1":
            print("turns out gothon are scared of bombs. He runs away and you activate the bomb. Looks like you'll have to find a way off the ship, and fast")
            return "victory"
        elif choice == "2":
            print("Yeah, Gothon have claws and armor. Not sure what you were thinking there")
            return "death"
        else:
            print("sorry, didn't understand that.")
            self.enter()

class CentralCorridor(Scene):

    def enter(self):
        print("Your ship has been overtaken by aliens! In fact, one alien is standing right in front of you. He looks pretty impressionable. Would you like to...")
        print("1. Attack It")
        print("2. Tell a Joke")
        choice = input('> ')
        if choice == "1":
            print("You don't even have any weapons on you. Sucks for you.")
            return "death"
        elif choice == "2":
            print("In the heat of the moment, you pull up the oldest, stupidest joke in the book. Seems like he... liked it, though? You pass through and get to the laser Weapons Armory.")
            return "victory"
        else:
            print("That doesn't make sense.")
            return self.enter()

class LaserWeaponArmory(Scene):

    def enter(self):
        print("In this room, there's a bomb with a keycode on it. It's locked in place right now, but getting the code correct could free it.")
        print("Scouring around, you learn that the code is 4 numbers long, and has at least one 1 in it.")
        choice = input('> ')
        if choice == "1111":
            print("That's right! Man, We really did a bad job at coming up with a secure password...")
            print("Next up, it's the Bridge.")
            return "victory"
        else:
            print("That's the wrong code... You accidentally detonate the bomb, destroying the ship and killing you.")
            return "death"

class EscapePod(Scene):

    def enter(self):
        print("It's the escape pod room! Looks like you've got a chance to get out! But, there are 3 escape pods. Which one is th safe one?")
        choice = input('> ')

        if choice == "1":
            print("You launch out of the spaceship and watch it explode. Congrats, you did it!")
            return "victory"
        elif choice == "2":
            print("Uh-oh, there was a gothon in this one. Before you have the chance to do anything, the gothon bites your head off.")
            return "death"
        elif choice == "3":
            print("This last pod won't even budge! You don't make it out before the explosion hits.")
            return "death"

map = Map(CentralCorridor())
engine = Engine(map)

engine.play()
