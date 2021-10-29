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

    virginia "I entered the police department."
    virginia "There weren't that many people, but maybe I can ask around."

    pause 0.5

    virginia "The letter..."
    virginia "I think it can tell me something about its author."

    call screen letter_natasha

label natasha_clue2:
     
     virginia "There's a kiss on this letter."
     virginia "Red... very sexy."

     call screen police_clue

label natasha:
    $ natasha_points = 0
    scene bg police clue with dissolve
    virginia "The red lipstick!"

    natasha "Girl. What are you doing here?"
    natasha "What is your name? Speak!"
    menu:
        "Vera Burova.":
            natasha "Do you think I cannot detect a lie when I hear one?"
            natasha "It is my job to seek the truth."
        "Virginia van Buren":
            $ natasha_points += 1
            natasha "Honesty. Not something I expect from an Amerikan."
            natasha "Your name sounds bourgeois. Is your character bourgeois as well?"
        "I won't tell you anything!":
            natasha "You do not need to tell me anything at all, Virginia van Buren."
            natasha "You are surprised I already know your name? Soviet intelligence is the greatest in the world!"

    natasha "Why have you come to USSR?"        
    menu:
        "For a vacation.":
            natasha "Yes, life is always a vacation to bourgeois kapitalists. You come to spend your money and look at us like animals."
            natasha "What luxury to live in idleness!"
        "I'm tired of capitalistic injustice.":
            $ natasha_points += 1
            natasha "Hm. Aren't we all? Perhaps you are wiser than a typical Amerikanski."
        "To find somebody.":
            natasha "How cryptic. You must know that we do not like secrets here in USSR."

    "And what are you going to do here in USSR?"        
    menu:
        "Study in one of the universities.":
            natasha "You still think like the bourgeois. Do you think you can change the world from your ivory tower?"
            natasha "Do you think that you can eliminate the class system by writing papers and reading books?"
            natasha "You are a child. We have no use for children."
        "I can be of use for KGB agents.":
            $ natasha_points += 1
            natasha "Do you know... I think you are right."
            natasha "If you are willing to sacrifice for Great Revolution, if you are willing to betray the country that has betrayed you... I believe we have a use for you."
        "Live my best life in the best country.":
            natasha "Selfish girl. Do not come here to seek the best life. Seek the life that is best for all!"

    natasha "Well, to be honest..."

    if natasha_points > 1:
        jump natasha_good_end
    else:
        jump natasha_bad_end

    return

label natasha_good_end:
    natasha "It was me. I sent the letter."
    natasha "I believed you could help in our glorious revolution, and I am glad to see I was correct."
    natasha "Girl. Will you join me for a drink of vodka?"
    natasha "I should like to get to know you better."
    natasha "Much better."
    scene bg natasha_good with fade

    pause 5

    return

label natasha_bad_end:
    natasha "You do not believe the things you say. You are an Amerikan spy!"
    natasha "You are under arrest. Guards! Send this american spy to GULAG!"
    scene bg natasha_bad with fade

    pause 5

    return