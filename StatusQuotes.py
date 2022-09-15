import random

quotesExtremelyLow = {
    0: "Visit me in the hospital.",
    1: "If I go any lower I'll end up in a coma.",
    2: "Where the apple juice at.",
    3: "Not even SSRI's will cure a feeling this low.",
    4: "It's not coming up anymore ;)",
    5: "I will eat EVERYTHING right now."
}

quotesLow = {
    0: "Shake those hands.",
    1: "Feeling a little dizzy.",
    2: "Give me some sugar baby.",
    3: "I feel tired."
}

quotesNormal = {
    0: "Nothing much, how are you?",
    1: "I should be in this range more often.",
    2: "Nothing to see here.",
    3: "I feel fine at the moment.",
    4: "I am not ill, my pancreas is just lazy."
}

quotesHigh = {
    0: "I should probably go for a walk.",
    1: "I just had something to eat.",
    2: "Dipping right now would be good for me."
}

quotesExtremelyHigh = {
    0: "It's so high, not even cocaine will give me a bigger rush.",
    1: "High on 6-(hydroxymethyl)oxane-2,3,4,5-tetrol.",
    2: "Don't think this will good for my nerves.",
    3: "No glasses will restore this eyesight.",
    4: "Prepare for the rollercoaster drop."
}


def getQuote(BG_value):
    """ Returns a random quote based on measurement

        Parameters:
        - Expects BG_value
    """
    
    if BG_value < 3:
        return random.choice(list(quotesExtremelyLow.values()))
    if BG_value > 3 and BG_value < 4:
        return random.choice(list(quotesLow.values()))
    if BG_value > 4 and BG_value < 10:
        return random.choice(list(quotesNormal.values()))
    if BG_value > 10 and BG_value < 13.3:
        return random.choice(list(quotesHigh.values()))
    else:
        return random.choice(list(quotesExtremelyHigh.values()))