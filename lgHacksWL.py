froshWL = input("Your current language: Spanish, French or Mandarin.")

if froshWL == "Spanish":
    spanishPL = input("Please input your current spanish placement. Type 1, 2, or Heritage.")
    if spanishPL == "1":
        print("Spanish 1, 2, 3, and then 4 or AP. Your choice. Although you are only required to take 2 years of a single language, taking up to 4 will send you to a better college.")
    elif spanishPL == '2':
        print("Spanish 2, 3, then 4 or AP. Your choice. This path is very good, as you already come into the language with some experience, and can build on it.")
    elif spanishPL == 'Heritage':
        print("""You have a slightly different path. You'd probably do Spanish Heritage 1 and 2, and then move on to AP Spanish Language and then AP Spanish Literature.
        This shows how you are connecting to your culture, while also expressing an interest in higher language.""")

if froshWL == "French":        
    frenchPL = input("Please input your current French placement. Type 1, or 2.")
    if frenchPL == "1":
        print("French 1, 2, 3, and then 4 or AP. Your choice. Although you are only required to take 2 years of a single language, taking up to 4 will send you to a better college.")
    elif frenchPL == '2':
        print("French 2, 3, then 4 or AP. Your choice. This path is very good, as you already come into the language with some experience, and can build on it.")

if froshWL == "Mandarin":
    mandarinPL = input("Please input your current spanish placement. Type 1, 2, or 3.")
    if mandarinPL == "1":
        print("Mandarin 1, 2, 3, and then 4 Honors or AP. Your choice. Although you are only required to take 2 years of a single language, taking up to 4 will send you to a better college.")
    elif mandarinPL == '2':
        print("Mandarin 2, 3, then 4 Honors or AP. Your choice. This path is good, as you already come into the language with some experience, and can build on it.")
    elif mandarinPL == '3':
        print("Mandarin 3, then 4 Honors or AP. Your choice. This path is very good, as you already come into the language with some experience, and can build on it.")
        


