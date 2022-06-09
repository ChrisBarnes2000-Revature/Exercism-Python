def response(hey_bob):
    def isQuestion(str): return str.strip().endswith("?");
    def isYelling(str): return str.strip().isupper();
    def isEmpty(str): return len(str.strip()) == 0;
    
    if isQuestion(hey_bob) and isYelling(hey_bob): return "Calm down, I know what I'm doing!"
    elif isYelling(hey_bob): return "Whoa, chill out!"
    elif isQuestion(hey_bob): return "Sure."
    elif isEmpty(hey_bob): return "Fine. Be that way!"
    else: return "Whatever."