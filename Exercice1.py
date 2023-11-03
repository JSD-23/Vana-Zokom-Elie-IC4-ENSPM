def lengthOfLastWord(s):
    # Votre code ici
    if len(s) == 0 :
        return 0
    else :
        mots = s.split(' ')
        return len(mots[-1])

print(lengthOfLastWord('Hello World'))
print(lengthOfLastWord(""))
