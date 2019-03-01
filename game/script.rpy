image badend = "badend.jpg"
image coffeeshop = "coffeeshop.jpg"
image goodend = "goodend.jpg"
image hello = "hello.jpg"
image jackfrost = "jackfrost.jpg"
image ohhey = "ohhey.jpg"
image romanticend = "romanticend.jpg"
image sexyend = "sexyend.jpg"
image smtv = "smtv.jpg"

define j = Character('Jack Frost', color="#110eed")
define m = Character('Me', color="#c8ffc8")
define n = Character('Nicolas', color="#D16587")

label start:

    play music "fl.mp3"

    scene coffeeshop

    "It's a Friday Morning and School was already in the process. But as usual, I needed my morning coffee so that my brain can function normally."

    "I was on my way to the coffee shop when I saw someone very very familiar..."

    m "Wait...."

    show hello

    m "Oh my God!!!!!!"

    "Everyone stared at me like I was crazy"

    hide hello

    show ohhey

    "He placed a finger on his lips"

    n "shhh....."

    "Then he winked at me!"

    "I can't believe it! What is Nicolas Cage doing here?"

    "He had always been my favourite actor and not to mention...."

    menu:

        "Your face is..."

        "Beautiful":

            jump beautiful

        "Magnificient":

            jump magnificient

        "Fabulous":

            jump fabulous

        "Your shoes....I like them":

            jump bad

        "...never mind, I just want SMT V":

            jump smt

label beautiful:

    n "I'm Beautiful? Why thank you!!"

    m "Sir... I-I love you! From the moment I set my eyes on you, I just knew you were so beautiful from the insidie and the ouside... and that I needed your babies!'"

    n "You... Those are the most wonderful words anyone had ever said to me..."

    n "Come, let us commence the baby-making process"

    hide ohhey

    show romanticend

    "Congratulations! You got the romantic ending!"

    return

label magnificient:

    n "I hope I look like a unicorn."

    m "Sir... You are by far my favourite actor ever!!! Can we... ummm...ummm"

    n "What is it, child? Spit it out!!!"

    "Next thing you knew, everything turned black."

    m "Where am I...?"

    n "Worry not. You passed out earlier so I dragged your body to the hospital."

    m "Mister Cage... Thank you"

    "And so he caged your heart softly.."

    hide ohhey

    show goodend

    "Congratulations! You got the good ending!"

    return

label fabulous:

    n "I know, right?"

    m "Sir! You have been my favourite actor! I- I-"

    n "Don't call me Sir... Call me Daddy."

    "And so they made love all night long and had beautiful children"

    hide ohhey

    show sexyend

    "Congratulations! You got the sexy ending!"

    return

label bad:

    n "Uhh.. thanks?"

    m "I-I...-"

    n "Umm... I think I need to go."

    m "NO! Don't leave me!!!"

    "I grabbed his arm with all my might"

    n "What??? Let go of me at once!"

    m "No! I love you!!!"

    n "Somebody help!!"

    "Someone from the coffee shop called the police and you were arrested."

    "You went crazy in your prison cell and swore to get Nicolas Cage with you"

    hide ohhey

    show badend

    "Better luck next time (Bad ending)"

    return

label smt:

    n "Hee Ho!!"

    m "Cage-senpai?"

    n "I can drop the act now. I am no Nic Cage I am..."

    hide ohhey

    show jackfrost

    j "JACK FROST!"

    j "Lemme tell you a secret young fella."

    j "I'M TIRED OF FUCKING PERSONA"

    j "I WANT A REAL SHEEN MEGOOMI TENSAY GAME ALREADY DAMMIT!"

    "Jack Frost burst into tears and cried against your chest."

    "...It felt good comforting Jack Frost tbh."

    hide jackfrost

    show coffeeshop

    "Wait Jack Frost is evolving...!"

    show smtv

    "Congratulations! Jack Frost evolved into SMT V! (True End)"

    return