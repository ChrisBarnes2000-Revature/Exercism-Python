def translate(text):
    ay = "ay"
    way = "way"
    consonant = ("B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","Y","V","X","Z")
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    vowel = ("A","E","I","O","U")

    pig_latin_string = ""
    words = text.lower().split()
    for user_word in words:
        # getting first letter and making sure its a string and setting it to uppercase
        first_letter = str(user_word[0]).upper()
        first_two_letters = str(user_word[0]).lower() + str(user_word[1]).lower()

        if first_letter in consonant:
            length_of_word = len(user_word)
            remove_first_letter = user_word[1:length_of_word]
            pig_latin=remove_first_letter+first_letter.lower()+ay
            pig_latin_string=pig_latin_string+" "+pig_latin
        
        elif first_two_letters in lst:
            user_word = user_word[2:] + user_word[:2] + 'ay'
        
        elif first_letter in vowel:
            pig_latin=user_word+ay
            pig_latin_string=pig_latin_string+" "+pig_latin

        else:
            print("?")
    return pig_latin_string.strip()