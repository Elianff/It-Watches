label dontanswer:
    "WHAT THE ACTUAL."
    "No you couldn't see anything."
    "Nothing at all."
    scene bg sleep onlayer farback at Position(ypos = 1200) with dissolve
    "Pretend to sleep."
    "zzz."
    "You're sleeping, you can't see any monster."
    "No monster at all."
    "It" "Hmm I guess you can't see me."
    "Yep!"
    "Can't see at all."
    "It" "I guess you would't mind then."
    "It" "If I stepped out of the closet."
    "OH WOW!"
    "YOU WOULD MIND ACTUALLY!"
    "There was a creak, followed by another."
    "It was moving closer."
    "Where was it..?"
    "Maybe just a peak?"
    "Surely it wouldn't notice?"
    scene bg room onlayer farback at Position(ypos = 1200) 
    show closesmile onlayer inyourface at Position(ypos = 1120) 
    
    "HOLY-"
    "It" "Well hello there."
    "It" "You're looking straight at me."
    "It" "Don't pretend you can't see me."
    "..."
    scene bg room onlayer farback at Position(ypos = 1200) 
    show smallsmile onlayer inyourface at Position(ypos = 1120) 
    "It" "Are you ignoring me?"
    "It" "That's not nice."
    menu:
        "What are you...Why are you here. WHY ME?":
            jump alotofquestions
        "Ignore it.":
            jump ignore

        