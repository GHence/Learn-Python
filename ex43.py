from sys import exit
from random import randint
from textwrap import dedent    # textwrap 模块的dedent函数。这个函数是为了写房间描述时使用三引号字符串

# 代码中有一个叫Scene的基类，包括所有场景的通用信息
class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "You mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of Planet #25 have invaded yopur ship and
        destroyed your entire crew. You are the last surviving
        member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in the brige, adn
        blow the ship up after getting into an escape pod.
        
        You're runing down the central corridor to the Weapons
        Armory when a Gothon jumps out, red scaly skin, dark grimy
        teeth, and evil clown costume flowing around his hate
        filled body. He's blocking the door to the Armory and
        abort to pull a weapon to blast you.    
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            Quick on the draw you yank out your blaster and fire
            it at the Gothon. His clown costume is flowing and
            moving around his body, which throws off your aim.
            Your laser hits his body , which throws off youe aim.
            Your laser hits his costume but misses him entirly.
            This completely ruins his brand new costume his mother
            bought him, which makes him him fly into an insane rage
            and blast you repeatedly in the face until you are
            dead. Then he eats you.            
            """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and
            slide right as the Gothon's blaster cranks a laser
            past your head. In the middle of your artful dodge
            your foot slipe and you bang your head on the metal
            wail and pass out. You wake uo shortly after only to
            die as the Gothon stomps on your head and eats you.
            """))
            return 'death'
        elif action == "tell a joke":
            print(dedent("""
            Lucky for you they made you learn Gothon insults in
            the academy. You tell the one Gothon joke you know:
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
            fur fvgf nebhag gur ubhfr. The Gothon stops, tris
            not to laugh, then busts out laughing and cat's move.
            While he's laughing you run up and shoot him square in
            the head putting him down, then jump throgh the Weapon Armory door.
            """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmoy(Scene):

    def enter(self):
        print(dedent(""""
        You do a dive roll into the Weapon Armory, crouch and scan
        the room for more Gothons that might be hiding. It's dead
        quite, too quite. You stand up and run to the far side of
        the lock closes forever and you can't get the bomb. The
        code is 3 digits.
        """))

        code = f"{randint(1,9)} {randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The lock buzzes one last time and then you hear a 
                sickening melting sound as the medchism is fused
                together. You decide to sit there, and finally the
                Gothons blow up the ship from their ship and you die.    
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a 
            sickeaning melting sound as the mechanism is fused
            together. You decide to sit there, and finally the
            Gothons blow up the ship from their ship and you die
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the netron desturct bomb
        under your arm and surprise 5 Gothons who are trying to
        take control of the ship. Each of them has an even uglier
        clown costume than the lat. They have't pulled their
        weapons out yet, as they see the active bomb under your
        arm and don't want to set it off.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons 
            and make a leap for the door. Right as you drop it a
            Gothon shoots you right in the back killing you. As
            you die you see another Gothon frantically try to
            disarm the bomb. You die konwing they will probably
            blow up when it goes off.
            """))
            return 'death'
        elif action == "slowly palce the bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and
            the Gothons put their hands up.......
            """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush nhhjhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
        """))
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
            You jump into pod {guess} and hit the 后面省略
            """))
            return 'death'
        else:
            print(dedent("""
            You jump into pod {guess} and hit the eject button.
            The pod easily slides out into space heading to
            the planet below. As it flies ti the planet, you look 
            back and see your ship implode then explode like a
            bright start, taking out the Gothon ship at the same
            thime. You won!
            """))

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmoy(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
