# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define natasha = Character("Natasha Vorobiova")

screen letter_natasha:
    imagemap:
        ground "natasha_text.png" 

        hotspot (756, 700, 175, 129) action Jump("natasha_clue2")

screen police_clue:
    imagemap:
        ground "bg police.jpeg" 

        hotspot (735, 398, 127, 181) action Jump("natasha")

label police:
    scene bg police with fade

    virginia "I entered a police department."
    virginia "There are not that many people, maybe I can ask around?"

    pause 0.5

    virginia "The letter itselft..."
    virginia "I think it can tell me something about its author."

    call screen letter_natasha

label natasha_clue2:
     
     virginia "Here's a kiss on this letter."
     virginia "Red... And sexy."

     call screen police_clue

label natasha:
    $ natasha_points = 0
    scene bg police clue with dissolve
    virginia "The red lipstick!"

    natasha "What is your name?"
    menu:
        "Vera Burova.":
            natasha "it mot true!"
        "Virginia van Buren":
            $ natasha_points += 1
            natasha "Exactly how I think."
        "I won't tell you anything!":
            natasha "Everyone? Even the burgies?"

    natasha "Why have you come to USSR?"        
    menu:
        "For a vacation.":
            natasha "..."
        "I'm tired of capitalism injustise.":
            $ natasha_points += 1
            natasha "..."
        "To find somebody.":
            natasha "..."

    "And what are you going to do here, in USSR?"        
    menu:
        "Study in one of the univercities.":
            natasha "..."
        "I can be of use for KGB agents.":
            $ natasha_points += 1
            natasha "Exactly how I think."
        "Live my best life in the best country.":
            natasha "..."

    natasha "Well, to be honest..."

    if natasha_points > 1:
        jump natasha_good_end
    else:
        jump natasha_bad_end

    return

label natasha_good_end:
    natasha "It was me. I've sent the letter."
    scene bg natasha_good with fade

    pause 5

    return

label natasha_bad_end:
    natasha "You are under arrest. Guards! Send this american spy to some GULAG!"
    scene bg natasha_bad with fade

    pause 5

    return