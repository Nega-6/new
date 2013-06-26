
import sys

class StoryPiece:
    def __init__(self, text):
        self.text = text
        self.choices = []
    def add_choice(self, choice):
        self.choices.append(choice)
    def run(self):
        print self.text

        
class StoryPiece:
    def __init__(self, text):
        self.text = text
        self.choices = []
    def add_choice(self, choice):
        self.choices.append(choice)
    def run(self):
        print self.text
        while True:
            data = sys.stdin.readline().rstrip()
            for choice in self.choices:
                if data == choice.command:
                    return choice.destination
            print "Nothing happened."

            
class Choice:
    def __init__(self, command, destination):
        self.command = command
        self.destination = destination
        
class End:
    def __init__(self, text):
        self.text = text

    def run(self):
        print self.text

        while True:
            sys.exit()

            
bed = StoryPiece ("""You awake with your alarm blaring in your ear. It is 8:00 in the
morning and you have to get to work. What do you do?""")

standing = StoryPiece ("""You rise slowly out of bed, reluctant to start the day. You stand in
the center of your bedroom and look around. Directly infront of you is
your computer table, you had left a game installing over night and it
is still not finished. To the right of the computer is the door to the
kitchen, and on the left is the door to the bathroom. You have to take
a shower, brush your teeth, and eat breakfest before you can go to
work. What do you do?""")

bathroom = StoryPiece ("""You enter the bathroom and look around, to your right is the shower,
and directly ahead is the sink as well as your toothbrush and
toothpaste. What do you do?""")

shower = StoryPiece ("""You stand in the shower for roughly ten minutes and do various shower
things before stepping out and drying off. All you have to do before
hitting the road is brush your teeth and get some food! What do you
do?""")

brush = StoryPiece ("""You have brushed your teeth and are starting to feel very hungry.
There is no direct path to the kitchen from here, but you have to get
there. What do you do?""")

back = StoryPiece ("""You're back in the bedroom. What do you do?""")

kitchen = StoryPiece ("""Last night you made a sandwich and left it out on the counter so that
you could save time. Its still there, staring at you in it's
magnificent glory. What do you do?""")

tasty = StoryPiece ("""You devour the sandwich as you move towards the door of the garage.
You're ready for the day so you get in your car. Just drive to work
and you can get on with your day.""")

oops = End ("""You get in the car and drive to work. But wait! You don't have a job!
You just went to McDonalds! And to make things worse! You never got
dressed, so you're naked! You got arrested for indecent exposure. GAME
OVER.""")

goodjob = End ("""You remembered to get dressed! And you also remembered you don't have
a job. Nothing else to do. YOU WIN.""")

bed.add_choice(Choice("Get up", standing))

standing.add_choice(Choice("Enter bathroom", bathroom))

bathroom.add_choice(Choice("Take shower", shower))

shower.add_choice(Choice("Get dressed", goodjob))

shower.add_choice(Choice("Brush teeth", brush))

brush.add_choice(Choice("Get dressed", goodjob))

brush.add_choice(Choice("Enter bedroom", back))

back.add_choice(Choice("Get dressed", goodjob))

back.add_choice(Choice("Enter kitchen", kitchen))

kitchen.add_choice(Choice("Eat sandwich", tasty))

tasty.add_choice(Choice("Drive", oops))

part = bed

while True:
    part = part.run()






