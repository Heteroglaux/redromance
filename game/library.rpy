# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define comradel = Character("Comrade L.")

screen letter_comrade:
    imagemap:
        ground "comrade_text.png" 

        hotspot (897, 530, 414, 165) action Jump("comrade_clue2")

screen library_clue:
    imagemap:
        ground "bg library.jpeg" 

        hotspot (1364, 717, 295, 180) action Jump("comrade")

label library:
    scene bg library with fade

    virginia "I entered a big andquiet library."
    virginia "There are not that many people, maybe I can ask around?"

    pause 0.5

    virginia "The letter itselft..."
    virginia "I think it can tell me something about its author."

    call screen letter_comrade

label comrade_clue2:
     
     virginia "Here's a quote in the end of the letter..."
     virginia "The last capitalist we hang shall be the one who sold us the rope."

     call screen library_clue

label comrade:
    $ comrade_points = 0
    scene bg library clue with dissolve

    virginia "The Capital!"
    virginia "The quote is definetely from the book."
    "I heard a pleasand voice behind my back."
    "???" "I see you have a good taste in literature."
    virginia "Excuse me?"
    "???" "It's Marx! I've read the book dozens of time."
    virginia "Maybe even quoted it... Somewhere?"
    "???" "Oh, definetely!"
    virginia "My name is Virginia."
    comradel "You can call me a comrade, Virginia. Comrade L."
    virginia "I was looking for someone who wrote me a letter."
    comradel "I think you were searching for something else."
    comradel "A better place, maybe?"
    virginia "..."
    "Comrade L. took the book and opened it on a random page."
    comradel "I think, the world nowadays is corrupted. Common people aren't living the lifes they deserve. Poorer only become poorer, while the rich constantly get richer."
    comradel "You know what the means of production are? How do you think, who should own them?"

    menu:
        "Whoever owns them by law.":
            comradel "The law only supports the unjust system!"
        "The working class":
            $ comrade_points += 1
            comradel "Exactly how I think."
        "Everyone!":
            comradel "Everyone? Even the burgies?"

    "What do you think about sex?"        
    menu:
        "Why do you ask?":
            comradel "..."
        "There's no sex in USSR.":
            $ comrade_points += 1
            comradel "..."
        "I like sex. Why not?":
            comradel "..."

    "What is the best political regime?"        
    menu:
        "Liberalism!":
            comradel "..."
        "Dictotorship of proletariat!":
            $ comrade_points += 1
            comradel "Exactly how I think."
        "Democrasy!":
            comradel "..."

    comradel "Well, to be honest..."

    if comrade_points > 1:
        jump comrade_good_end
    else:
        jump comrade_bad_end

    return

label comrade_good_end:
    comradel "It was me. I've sent the letter."
    scene bg comrade_good with fade

    pause 5

    return

label comrade_bad_end:
    comradel "You better go. USSR is not a place for you to be."
    scene bg comrade_bad with fade

    pause 5

    return
