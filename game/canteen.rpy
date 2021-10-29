# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ulyana = Character("Uliana")

screen letter_ulyana:
    imagemap:
        ground "ulyana_text.png" 

        hotspot (617, 203, 300, 265) action Jump("ulyana_clue2")

screen canteen_clue:
    imagemap:
        ground "bg canteen.jpeg" 

        hotspot (1586, 366, 145, 235) action Jump("ulyana")

label canteen:
    scene bg canteen with fade

    virginia "I entered a big canteen."
    virginia "There are not that many people, maybe I can ask around?"

    pause 0.5

    virginia "The letter itselft..."
    virginia "I think it can tell me something about its author."

    call screen letter_ulyana

label ulyana_clue2:
     
     virginia "Here's a glass stain on this letter."
     virginia "Smells... Like alcohol."

     call screen canteen_clue

label ulyana:
    $ ulyana_points = 0
    scene bg canteen clue with dissolve
    virginia "The Vodka!"

    ulyana "What is your favourite color?"
    menu:
        "Green":
            ulyana "The law only supports the unjust system!"
        "Red":
            $ ulyana_points += 1
            ulyana "Exactly how I think."
        "Blue":
            ulyana "Everyone? Even the burgies?"

    ulyana "What do you do in your spare time?"        
    menu:
        "Riding horses!":
            ulyana "..."
        "Working MORE!":
            $ ulyana_points += 1
            ulyana "..."
        "Having flashbacks about my parents' tragic death.":
            ulyana "..."

    "Choose a drink to share with me!"        
    menu:
        "Champagne.":
            ulyana "..."
        "Vodka!":
            $ ulyana_points += 1
            ulyana "Exactly how I think."
        "Red Russian.":
            ulyana "..."

    ulyana "Well, to be honest..."

    if ulyana_points > 1:
        jump ulyana_good_end
    else:
        jump ulyana_bad_end

    return

label ulyana_good_end:
    ulyana "It was me. I've sent the letter."
    scene bg ulyana_good with fade

    pause 5

    return

label ulyana_bad_end:
    ulyana "You are already too drunk, gosh. Let me show you the exit."
    scene bg ulyana_bad with fade

    pause 5

    return