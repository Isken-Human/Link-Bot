#Function that takes masseges from user and replys to them
def smart_responses(reply_text):
    #setting user masseges and using .lower() to make it easyer to work with masseges
    user_message = str(reply_text).lower()

    if user_message in ("hello", "hi", "привет", "здарова"):
        return "Hi! Whats up"

    if user_message in ("who are you", "who are you?", "ты кто", "ты кто?"):
        return "I am link bot!\nI give links to your online classes!"

    if user_message in ("можно линк на калкулус", "можно линк калкулус"):
        return "Calculus: https://zoom.us/j/4654536993"

    if user_message in ("можно линк на турецкий ктл", "можно линк турецкий ктл", "турецкий ктл"):
        return "Turkish KTL: https://zoom.us/j/3473699064"
    
    if user_message in ("можно линк на турецкий", "можно линк турецкий", "турецкий oth"):
        return "Turkish OTH: https://zoom.us/j/97174914268"

    if user_message in ("можно линк на дискретку","можно линк дискретка"):
        return "Discrete math: https://zoom.us/j/4654536993"

    if user_message in ("Можно линк на обж","можно линк обж","линк обж"):
        return "Life safety: https://us04web.zoom.us/j/2784975745?pwd=SUFPZVlHMkhrb2F0RGVYak1MSTVhQT09 \nPassword: 1234"

    if user_message in ("можно линк на ооп","можно линк на питон","линк пайтон"):
        return "Object Oriented  Programming: https://ocs.iaau.edu.kg/course/view.php?id=85 \nGo to latest BBB class"

    if user_message in ("можно линк на английский","можно линк английский","можно ссылку на инглиш"):
        return "English: https://meet.google.com/nyx-pcwi-vwz"

    if user_message in ("можно линк на матан","можно линк на алгебру","можно линк алгебра"):
        return "Algebra and Geometry: https://zoom.us/j/5856122793 \nPassword : @MATHMAN"

    if user_message in ("можно ссылку на русский суракан","можно линк русский суракан","русский суракан"):
        return "Russian language Surakan: https://zoom.us/j/96966924568"

    if user_message in ("можно линк на русский гулина","можно ссылку русский гулина","русский гулина"):
        return "Russian language Gulina: https://zoom.us/j/8314051374?pwd=TVBDanAvYllTVEp6VkRiZ21Kempwdz09 \nPassword: astra123!"

    if user_message in ("можно ссылку физра для девочек","можно линк физра девочкам","физра девочки"):
        return "Physical training for girls: https://zoom.us/j/95827906871?pwd=MGRsWGVRVmM1MVFSb29ZMUVsZ1JUZz09"

    if user_message in ("можно линк физра пацаны","можно ссылку на физру","физра для мальчиков"):
        return "Physical training for boys: https://zoom.us/j/95304954695?pwd=cWFMcXcwemdoVG5PLzJwZWNEZUxwdz09"
    if user_message in ("пиздец"):
        return "Воистину пиздец"