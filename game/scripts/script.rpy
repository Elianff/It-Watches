# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    play music "audio/itlurks.wav" loop

    default persistent.parallax_on = True

    scene bg room onlayer farback at Position(ypos = 1200)
    #show bg room onlayer back at Position(ypos = 1200)
    #show bg doorwindow onlayer front at Position(ypos = 1140)
    #show bg bed onlayer inyourface at Position(ypos = 1120)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # These display lines of dialogue.

    "You woke up in the middle of the night."
    "That sucks..you had to wake up for work in the morning.."
    "Checking the time, it was 3 am."
    "Great..you still had time to sleep."
    "And of course your roommates were still awake."
    "You wish you were unemployed too..."
    "Ever since you moved in, you have been waking up at unholy hours."
    "It was getting out of hand."
    "What will it take for you to sleep a whole 8 hours?"
    "Uninterupted."
    "Settling down, you try to go back to sleep."

    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve

    "Maybe if you close your eyes.."

    scene bg open onlayer farback at Position(ypos = 1200) with dissolve

    "There's no use.."
    "You can't sleep."
    "Huh."
    "Did you leave your closet door open?"
    "That's odd..."
    "You would have remembered."
    "Oh well."

    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve
    "You must be seeing things."
    "Nothing sleep won't help."
    "Just have to stay like this for a little."
    "Roommates" "CHUG CHUG CHUG."
    "Oh for.."

    scene bg hand onlayer farback at Position(ypos = 1200) with dissolve
    "Would it kill them to shut up?"
    "It's 3 am.."
    "And you made it VERY clear you were going to sleep."
    "..."
    "You cover your ears with a pillow."
    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve
    "La la la."
    "I can't hear you."
    "..."
    "What a surprise!"
    "You're still awake!"
    "Yayy!"
    "Not. Yay."
    "You sigh as you try to get comfortable in bed."
    "You hear your roommates creaking around."
    "Great now even your neighbors below will hate you."
    "It kind of seemed close though.."
    "Did one of them sneak in?"
    scene bg room onlayer farback at Position(ypos = 1200) with dissolve
    "..."
    "Huh."
    "Interesting."
    "Your closet was closed."
    "God damnit you were so tired."
    "You scan the room only to find no roommate."
    "Maybe you should ram your head into the headboard!"
    "That will send you straight to sleep!"
    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve
    "Please oh please go to sleep."
    "You're sick and tired."
    scene bg hand onlayer farback at Position(ypos = 1200) with dissolve
    "..."
    "Are you seeing that correctly?"
    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve
    pause 1.0
    scene bg open onlayer farback at Position(ypos = 1200) with dissolve
    "What's going on..?"
    "You hear the villains laugh outside."
    "Are they pulling a prank on you??"
    "GREAT!"
    "Couldn't they have waited until oh..I don't know.. THE WEEKEND?"
    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve
    "You're not letting them win."
    "You hear a knock."
    "Nope."
    "Not waking up."
    "Another knock."
    scene bg face onlayer farback at Position(ypos = 1200) with dissolve
    "You" "What..What is it? What could it possibily be to wake me up before work?"
    "..."
    "Um."
    "Don't move."
    "Whatever you do..what.."
    "Were you seeing things?"
    "Why was there a..thing.. in your closet?"
    "And why was it smiling..?"
    "Surely this is a practical joke."
    "Ahaha where were the cameras?"
    "You were scared to blink."
    "To fall asleep."
    "To look away."
    "It made direct eye contact, and if you broke it.."
    "What would happen?"
    "What were you supposed to do?"
    "You inch your hand towards your phone."
    "It" "You can see me."
    "..."
    "It" "Right?"
    menu: 
        "You are NOT answering that.":
            jump dontanswer
        "No I can't see anything.":
            jump answer



    

    return
