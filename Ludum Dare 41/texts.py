intro_text = """
==================================================
==================================================

        The Pond: An Unexpected Journey
        
  
  Genre: Walking Simulator + Terminal Based Game
  

  Game by StaNov  (www.StaNov.cz)

  Created for Ludum Dare 41

  Theme: Combine 2 Incompatible Genres
  
==================================================

"""

step_texts = [
    "You stand by a big tree. It is a really beautiful one.\n\n"
    "On the horizon, you can see an even more beautiful pond.\n\n"
    "You really feel like you want to swim a bit in it.\n\n"
    "It’s quite far, but you really want to touch the water with your body.\n\n"
    "So you decided to go there.\n\n"
    "You can start your journey by typing 'step'.",

    "Congratulations! You took one step towards the pond.\n\nTry another one!",

    "You took another step to the pond.\n\nAh! The warm water is getting closer!\n\nGo on, you're doing great!",

    "And another step!",

    "And another one.",

    "...",

    "Yea, it’s really quite far.\n\n"
    "As I mentioned before.",

    "Left foot.",

    "Right foot.",

    "Pressing 'arrow up' doesn't repeat the command, sorry...",

    "Left foot.",

    "Right foot.",

    "Left foot.",

    "Aaaaaand... another left foot!\n\n"
    "Because of all the joy of walking, you jumped into the air!\n\n"
    "Weee!",

    "Right foot.",

    "Fun fact: There is an event in Brno where people walk around the city.\n\n"
    "One hundred kilometers during 24 hours.\n\n"
    "Crazy people.",

    "Yea, I mentioned it because I live in Brno.",

    "Brno is the biggest city in Czechia.",

    "...",

    "Well, it isn't.\n\n"
    "But people from Prague get angry when we say it to foreigners who don’t already know.",

    "Ha ha.",

    "But foreigners haven’t even noticed that Czechoslovakia has split into two states.",

    "It was in 1993.",

    "There, that’s an interesting history fact you learnt today!",

    "By the way, Czechia is the state where Kingdom Come Deliverance is placed and developed.",

    "Also Factorio is developed by Czechians.",

    "And Chameleon Run.",

    "And Shadowgun Legends.",

    "And Chuchel.",

    "And many others.",

    "...",

    "So!",

    "You slowly progress to the pond.\n\n"
    "But you don’t even mind that the journey is so long because you are so entertained by the narrative!",

    "And you don't need to think about what to type because you are doing it automatically!",

    "Left foot.",

    "Right foot.",

    "Did I mention the weather?\n\n"
    "It’s really beautiful. Sunny and warm.",

    "The grass around you is completely green and fresh.\n\n"
    "As you can see.",

    "Well, you could see it if this wasn’t a text game.\n\nJust pretend then.",

    "(IT Crowd reference)",

    "Anyway...",

    "Left foot!",

    "Right foot.",

    "A little tip: You can read the text in Morgan Freeman’s voice for better mood.",

    "Please do so and add me some points in the mood category later.\n\n"
    "Otherwise it is your fault that you didn’t, so don’t blame me.\n\n"
    "Thanks.",

    "You know what? We can meditate a bit!",

    "Let’s be quiet for some next steps.",

    "...",

    "...",

    "Focus on your breathing to calm your mind.",

    "Inhale.",

    "...",

    "Exhale.",

    "...",

    "...",

    "If you played some of my older games, you know I also create shitty graphics for Ludum Dare games.",

    "But today there is no time for that.\n\n"
    "So you can have a shitty ASCI picture of the road you are walking on.",

    """
                      /  \\
                     /    \\
                    /      \\
                   /    |   \\
                  /    /     \\
                 /    /       \\
                /     |        \\
""",

    "It should have been seen from a perspective but it doesn't.\n\n"
    "Nevermind then.",

    "And by the way, the tree from the beginning looked like this:",
    """
                   ----------------
                /                   \\
            /      /       \\   \\       \\
        |      /         /     \\     \\       \\
        |         /           \\         \\
           |    /       /     \\     \\     \\
              \\    /   /     \\      \\  \\
                     -----------
                     |     |   |
                     |     |   |
                     |     |   |
                     |    /    |
                     |   /     |
                     |   |     |
                     |   |     |
                     |   |     |
""",
    "There you have some serious art!",

    "I also create some crazy kazoo soundtracks.",

    "But not this time, sorry.",

    "This game was created only in three hours.",

    "I didn’t want to participate at all.\n\n"
    "But when I saw the theme I was like “OMG OMG, it’s gonna be fun, I have to do it!”",

    "So here we go.",

    "I created better games in the past, I can say that.",

    "You can say that.",

    "But hey, you are almost there, so don’t stop now!",

    "Left foot.",

    "Right foot.",

    "The summer breeze is touching your face.",

    "For even better mood you can find a youtube video with the summer breeze sound.",

    "Nah, as a good person, I found it for you:\n\n"
    "https://www.youtube.com/watch?v=eSGtSq_i7dk",

    "It is 8 hours long. Just enough to finish this game.",

    "Just kidding!",

    "(kappa)",

    "Alright, back to the grassy road you walk on.",

    "Left foot.",

    "Right foot.",

    "Do you know how much did you practice the typing skills while playing this game?",

    "And did you know that you can type only “s” instead of “step”?",

    "Yea, I implemented it for debug reasons because I was too bored\n"
    "in the end of the development to type step step step again again again.",

    "So now when you know it, you can just run to the pond!",

    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",
    "Left foot.",
    "Right foot.",

    "SLOW DOWN!",
    "SLOW DOWN!!!",
    "SLOW DOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",

    "If you jump into the water like that you will get sick!",

    "So...",

    "Just a little bit of calm slow steps.",

    "It really is almost the end, I promise.",

    "You can see the pond.",

    "You are almost there.",

    "You can feel the water in the air.",

    "The water is reflecting the sky.",

    "It is so beautiful.",

    "Only three steps and you will be swimming in it.",

    "You are so grateful that you didn’t stop in the middle of the road.",

    "You bend your knees and jump into the water...",

    "The world is perfect.",

    "Thanks for playing :)\n\n"
    "Here, you can have a kazoo interpretation of the victory theme from Final Fantasy VIII.\n\n"
    "https://www.youtube.com/watch?v=6AAw_TnsZB0\n\n"
    "(hi, Joshua McLean!)\n\n"
    "And you can drop there a comment for the people who also got to the pond :)\n\n"
    "THE END!",
]
