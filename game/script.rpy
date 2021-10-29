# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define virginia = Character("Virginia")

screen envelope:
    imagemap:
        idle "letter.png" 
        hover "letter_hover.png" 

        hotspot (853, 388, 203, 218) action Jump("clue1_comrade")
        hotspot (635, 623, 321, 107) action Jump("clue1_natasha")
        hotspot (1009, 186, 248, 193) action Jump("clue1_ulyana")

screen comrade_street:
    imagemap:
        ground "bg street.jpeg"

        hotspot (79, 185, 478, 843) action Jump("comrade_wrong_building")
        hotspot (1412, 241, 287, 574) action Jump("comrade_wrong_building")
        hotspot (1049, 263, 305, 624) action Jump("library")
        

screen natasha_street:
    imagemap:
        ground "bg street.jpeg"

        hotspot (79, 185, 478, 843) action Jump("natasha_wrong_building")
        hotspot (1412, 241, 287, 574) action Jump("police") 
        hotspot (1049, 263, 305, 624) action Jump("natasha_wrong_building")


screen ulyana_street:
    imagemap:
        ground "bg street.jpeg"

        hotspot (79, 185, 478, 843) action Jump("canteen")
        hotspot (1412, 241, 287, 574) action Jump("ulyana_wrong_building")
        hotspot (1049, 263, 305, 624) action Jump("ulyana_wrong_building")


# The game starts here.

label start:

    scene bg room

    show virginia idle

    virginia "My world was a mess over the last two months."
    virginia "I was devastated after breaking up with Skye and my rich Aunt June kept trying to interfere in my life."
    virginia "But a week ago I received this letter... from the USSR."
    virginia "Someone had written that they'd admired my work with the United Working Alliance, and that they wanted to invite me to the USSR."
    virginia "They said they believed we could build a better, communist world together."

    scene bg street with fade

    virginia "I decided to take a trip to Moscow."
    virginia "The letter I received was completely anonymous. No name or address... only the warm words of love and admiration."
    virginia "I didn't have a lot of hope, but perhaps I could find the author."
    virginia "I think there are couple of obvious clues on the envelope."

    call screen envelope

    # This ends the game.
    return

label clue1_comrade:

    virginia "Here's a wax stamp with hammer and sickle."
    virginia "Maybe the symbol can lead me somewhere?"

    call screen comrade_street

    return    


label clue1_natasha:

    virginia "A Top Secret stamp. Looks very official."
    virginia "Could this letter be sent from the Soviet Police Department?"

    call screen natasha_street

    return

label clue1_ulyana:

    virginia "There's a factory bulding depicted on this stamp."
    virginia "I believe I've seen the same factory in the city."

    call screen ulyana_street

    return

label comrade_wrong_building:
    
    virginia "Hmm, I don't think I need go there."

    call screen comrade_street

    return

label natasha_wrong_building:
    
    virginia "Hmm, I don't think I need go there."

    call screen natasha_street

    return


label ulyana_wrong_building:
    
    virginia "Hmm, I don't think I need go there."

    call screen ulyana_street

    return
