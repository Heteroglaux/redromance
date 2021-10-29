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

    show virginia idle at right with moveinright

    virginia "I entered a large, quiet library."
    virginia "There aren't many people here. Maybe I can ask around?"

    hide virginia with fade

    virginia "The letter!"
    virginia "I think it can tell me something about its author."

    call screen letter_comrade

label comrade_clue2:
     
     virginia "There's a quote in the end of the letter..."
     virginia "The last capitalist we hang shall be the one who sold us the rope."
     virginia "I think I've read it somewhere..."

     call screen library_clue

label comrade:
    $ comrade_points = 0
    scene bg library clue with dissolve

    virginia "Das Kapital!"
    virginia "The quote is definitely from the book."
    "I heard a pleasant voice behind my back."

    show comrade idle at right with moveinright
    "???" "I see you have a excellent taste in literature."

    show virginia flip at left with moveinleft
    virginia "Excuse me?"
    "???" "It's Marx! I've read the book dozens of times."
    virginia "Maybe even quoted it somewhere?"
    "???" "Oh, without a doubt!"
    virginia "My name is Virginia."
    comradel "You may call me a comrade, Virginia. Comrade L."
    virginia "I was looking for someone who wrote me a letter."
    comradel "I think you were searching for something else."
    comradel "A better place, maybe?"
    comradel "A place where the worker is celebrated, perhaps."
    virginia "..."
    "Comrade L. took the book and opened it on a random page."
    comradel "As you must know, the world nowadays is corrupt. Common people aren't living the lives they deserve. The poor only become poorer, while the rich get richer."
    comradel "Yet who controls the means production? Who provides the sweat and toil?"
    comradel "Whom do you think should receive the rewards of their work?"

    menu:
        "Everyone!":
            comradel "Everyone? Even the bourgeois? Even those who fatten themselves on our labor?"
        "Whomever owns them by law.":
            comradel "You speak like a child. The law exists only to support the unjust system!"
        "The working class.":
            $ comrade_points += 1
            comradel "You are wise for your years, Miss Virginia. Indeed, the workers should own their own work."

    comradel "What do you think about sex?"        
    menu:
        "Why do you ask?":
            comradel "Your evasiveness does not inspire confidence."
        "There is no sex in the USSR.":
            $ comrade_points += 1
            comradel "Indeed. Sex contributes nothing to the glory of the worker."
        "I like sex. Why not?":
            comradel "I see you are still a child, wasting your time with idle fancies."
            comradel "I was once like you. Now I derive pleasure only from the struggle of the proletariat."

    comradel "What is the best political regime?"        
    menu:
        "Dictatorship of the proletariat!":
            $ comrade_points += 1
            comradel "Exactly! We who control the means of production also must control the product itself."
            comradel "We have power, if only we will take it!"
        "Liberalism!":
            comradel "The philosophy of cowards!"
            comradel "The ruling classes will always turn liberalism to their own ends."
        "Democracy!":
            comradel "You Amerikanskis believe so dearly in your dying system."
            comradel "While your poor die in the streets, you celebrate their right to vote."
            comradel "Little comfort is democracy to those who are forgotten their country."

    comradel "Well, to be honest..."

    if comrade_points > 1:
        jump comrade_good_end
    else:
        jump comrade_bad_end

    return

label comrade_good_end:
    comradel "It was I. I sent the letter."
    comradel "I hoped that it would reach one with a sound mind and brave heart."
    comradel "Miss Virginia. I welcome you to the Union of Soviet Socialist Republics."
    comradel "I call you comrade and equal now."
    scene bg comrade_good with fade

    pause 10

    return

label comrade_bad_end:
    comradel "You had better go. The USSR is not a place for you to be, Amerikanski."
    comradel "Go back to your precious Amerika and live in your excesses."
    comradel "You will not be a part of our glorious revolution."
    scene bg comrade_bad with fade

    pause 10

    return
