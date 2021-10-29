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

    virginia "My life was a mess the last two months."
    virginia "I wasn't feeling too good after breaking up with Skye..."
    virginia "But a week ago I received this love letter... From USSR."
    virginia "Somebody has written that they admire my work in United Working Alliance. And thet they want to invite me to USSR."
    virginia "To build a better, communist world together."

    scene bg street with fade

    virginia "I decided to take a trip to Moscow."
    virginia "The letter is completely anonymus. No name or address... Only the warm words of love and admiration."
    virginia "I don't have a lot of hope, but maybe I can find the author."
    virginia "I think there are couple of obvious clues on the envelope."

    call screen envelope

    # This ends the game.
    return

label clue1_comrade:

    virginia "Here's a wax stamp with this symbol."
    virginia "Maybe the symbol can lead me somewhere?"

    call screen comrade_street

    return    


label clue1_natasha:

    virginia "A Top Secret stamp. Looks very policey."
    virginia "Could this letter be sent from the Soviet Police Department?"

    call screen natasha_street

    return

label clue1_ulyana:

    virginia "Here's a factory bulding depicted on this stamp."
    virginia "I believe I've seen the same factory in the city."

    call screen ulyana_street

    return

label comrade_wrong_building:
    
    virginia "Hm-m-m, I don't think I need go there."

    call screen comrade_street

    return

label natasha_wrong_building:
    
    virginia "Hm-m-m, I don't think I need go there."

    call screen natasha_street

    return


label ulyana_wrong_building:
    
    virginia "Hm-m-m, I don't think I need go there."

    call screen ulyana_street

    return
