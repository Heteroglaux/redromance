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

    virginia "I entered a large canteen."
    virginia "There aren't many people here. Maybe I can ask around?"

    pause 0.5

    virginia "The letter..."
    virginia "I think it can tell me something about its author."

    call screen letter_ulyana

label ulyana_clue2:
     
     virginia "There's a glass stain on this letter."
     virginia "Smells... Like alcohol."

     call screen canteen_clue

label ulyana:
    $ ulyana_points = 0
    scene bg canteen clue with dissolve
    virginia "The Vodka!"
    ulyana "We all drink vodka, silly girl."
    ulyana "What are you doing here?"
    virginia "I followed this letter."
    virginia "I want to help the cause."
    ulyana "Do you really? Then let me ask you some questions."

    ulyana "What is your favourite color?"
    menu:
        "Green":
            ulyana "The color of Amerikan money! The beginning and end of all Amerikan thinking. How typical."
        "Red":
            $ ulyana_points += 1
            ulyana "Hah! Yes. The color of power. Of strength. Of community."
            ulyana "And... your very fetching hair."
        "Blue":
            ulyana "A color for children. I do not like children."

    ulyana "What do you do in your spare time?"        
    menu:
        "Riding horses!":
            ulyana "Riding horses! A hobby for the truly bourgeois. How wonderful to spend your time with such idle fancies!"
        "Working MORE!":
            $ ulyana_points += 1
            ulyana "Yes!! You think as I do."
            ulyana "Only by working may we break our chains and contribute to the collective good."
        "Having flashbacks about my parents' tragic death.":
            ulyana "Bah. We have no need of more Chekhovs or Tolstoys."
            ulyana "The time for melodrama is over. We must be the architects of our own good!"

    "Choose a drink to share with me!"        
    menu:
        "Champagne.":
            ulyana "Typical Amerikanski, trying to throw your money around."
            ulyana "Money does not impress me, devochka. Only the strength of your will."
        "Vodka!":
            $ ulyana_points += 1
            ulyana "You have excellent taste. A simple drink is the best."
            ulyana "Vodka makes us strong and warm!"
        "Red Russian.":
            ulyana "Hah! You drink like a baby."
            ulyana "I am sorry, little one. I am afraid I do not have a bottle to feed you with."

    ulyana "Well, to be honest..."

    if ulyana_points > 1:
        jump ulyana_good_end
    else:
        jump ulyana_bad_end

    return

label ulyana_good_end:
    ulyana "It was me. I sent the letter."
    ulyana "I hoped that I would see your strength, and indeed, you have proven it."
    ulyana "Come. Drink with me. It will make you feel warm inside."
    ulyana "And perhaps we can share our warmth together."
    scene bg ulyana_good with fade

    pause 5

    return

label ulyana_bad_end:
    ulyana "You are already too drunk! What a child. I do not associate with children."
    ulyana "You are very pretty, but I need strength. Come back when you have some."
    scene bg ulyana_bad with fade

    pause 5

    return