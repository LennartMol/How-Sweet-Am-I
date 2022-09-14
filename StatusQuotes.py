import random

quotesExtremelyLow = {
    0: "Visit me in the hospital.",
    1: "If I go any lower I'll end up in a coma.",
    2: "Where the apple juice at."
}

quotesLow = {
    0: "Shake those hands.",
    1: "Feeling a little dizzy.",
    2: "Give me some sugar baby.",
    3: "It's not going up."
}

quotesNormal = {
    0: "Nothing much, how are you?",
    1: "I should be in this range more often.",
    2: "Nothing to see here."
}

quotesHigh = {
    0: "High on 6-(hydroxymethyl)oxane-2,3,4,5-tetrol.",
    1: "This can't be good for my nerves.",
    2: "I am not ill, my pancreas is just lazy.",
    3: "No glasses will restore this eyesight."
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
    else:
        return random.choice(list(quotesHigh.values()))