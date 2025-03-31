text = open("BARNEOUD Valentin.txt", "r")
AncienMessage = open("AncienMessage.txt","r")
readedText = AncienMessage.read()

def FunctionDecode(Text):
    cleanedText = readedText.split(' ')
    TextParLettre=[]
    for i in range(len(cleanedText)):
        cleanedText[i]= cleanedText[i].lower()
        flag=False
        for j in range(len(TextParLettre)):
            if cleanedText[i] == TextParLettre[j]:
                flag = True
        if flag == False:
            TextParLettre.append(cleanedText[i])
    return(TextParLettre)

print (FunctionDecode(AncienMessage))
ancienmessage=FunctionDecode(AncienMessage)

def enleveMauvaisMot(bonneList):
    mauvaisMot = ['rhubarb',  'watermelon', 'ximenia', 'nut', 'zucchini',
'blackberry', 'vine', 'cranberry',
 'durian', 'papaya', 'huckleberry', 'jujube', 'xerophyte', 'elderberry',
'tangerine', 'satsuma',
 'kiwi', 'victoria', 'lime', 'saffron', 'ugni', 'rasp', 'kale', 'avocado',
'xigua', 'ugly',
 'waxberry', 'eggplant', 'honeydew', 'lychee', 'dragonfruit', 'zinfandel',
'raspberry', 'guava',
 'indian', 'fig', 'orange', 'yuzu', 'date', 'tamarind', 'yam', 'strawberry',
'hawthorn', 'apple',
 'nectarine', 'cherry', 'fennel', 'elderflower', 'quandary', 'blueberry',
'quandong', 'zest',
 'wildberry', 'yellow', 'apricot', 'onion', 'cantaloupe', 'nutmeg',
'persimmon', 'mandarin', 'olive','lemon', 'tamarillo', 'ugli', 'mango', 'grape', 'banana', 'jackfruit','gooseberry', 'vanilla','mulberry', 'kumquat', 'peach', 'feijoa']
    flag = False
    listeenl=[]
    for i in range(len(bonneList)):
        flag == False
        for j in range (len(mauvaisMot)):
            if mauvaisMot[j]== bonneList[i]:
                flag=True
        if flag == False :
            listeenl.append(bonneList[i])
    return(listeenl)

print(enleveMauvaisMot(FunctionDecode(AncienMessage),))



def TrieurText(teeext):
    if not teeext:
        return []
    return (
        TrieurText([x for x in teeext[1:] if x < teeext[0]]) + [teeext[0]] + TrieurText([x for x in teeext[1:] if x >= teeext[0]])
    )



def FinalText(TExt,textadecode):
    finalText=[]
    for i in range (len(textadecode)):
        for j in range (len(TExt)):
            if textadecode[i] ==TExt[j]:
                finalText.append(j+1)
    return(finalText)



def FinalFunction(TExt):
    fffinal = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9]
    for i in range(len(TExt)):
        number = TExt[i]
        if number < 35:
            fffinal.append(alphabet[number])
    return (fffinal)

















