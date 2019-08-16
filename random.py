import random
NegativeWord={
  'glum':-1,
  'gloomy':-1,
  'cloudy':-1,
  'dim': -1,
  'dull':-1,
  'upset':-1,
  'low':-1,
  'bad':-1,
  'grim':-1,
  'unconfident':-1,
  'self conscious':-1,
  'betrayed':-1,

  'somber':-2,
  'downcast':-2,
  'unhappy':-2,
  'troubled':-2,
  'sad':-2,
  'blue':-2,
  'crummy':-2,
  'cheerless':-2,
  'alone':-2,
  'angry':-2,
  'anger':-2,

  'stressed':-3,
  'disheartened':-3,
  'miserable':-3,
  'discuraged':-3,
  'dismal':-3,
  'sorrowful':-3,
  'horrible':-3,

  'beat down':-4,
  'down':-4,
  'low':-4,
  'bumed out':-4,

  'miserable':-5,
  'melancholy':-5,
  'destroyed':-5,
  'hurting':-5,
  'weaping':-5,
  'crying':-5,
  'nothing':-5,
  'empty':-5,
  'numb':-5,

  'dejected':-6,
  'disparing':-6,
  'distrought':-6,
  'neglected':-6,

  'diconsolate':-7,
  'depressed':-7,
  }
PositiveWord={

  'good':1,
  'happy':1,
  'glad':1,
  'cheerful':1,
  'merry':1,
  'jolly':1,
  'content':1,
  'care free':1,
  'confident':1,
  'okay':1,
  'fine':1,

  'joyous':2,
  'lively':2,
  'blissful':2,
  'peppy':2,
  'chirpy':2,
  'chipper':2,
  'upbeat':2,
  'great':2,

  'sweet':3,
  'awesome':3,
  'trilled':3,
  'gleeful':3,
  'perky':3,
  'playful':3,
  'delighted':3,
  'delightful':3,
  'bubbly':3,
  'wonderful':3,
  'giggly':3,

  'zestful':4,
  'excited':4,
  'spunky':4,
  'gutsy':4,
  'fiery':4,
  'epic':4,

  'enthusiastic':5,
  'ecstatic':5,
  'elated':5,
  'exultant':5,

  'euphoric':6,
  'exhilarated':6,

  'boisterous':7,
  'rambunctious':7,
  'potato':7,
  }
nuetralWord={

   'exhausted':1,
   'tired':1,
   'sleepy':1,
   'drowsy':1,

   'energetic':0,
   'jittery':0,
   'normal':0,
   'bored':0,
   'calm':0,
   'relaxed':0,
   'inactive':0,
   'lazy':0,
   'unmotivated':0,
   'overwhelmed':0,
   }
def smallTalk(resp):

    print("Would you like to talk?")
    print("")
    resp = input("  ")
    resp = resp.lower()
    print("")

    if resp == "yes" or resp == "Yes" or resp == "sure" or resp =="Sure" or resp =="yup" or resp =="Yup" or resp =="all right"or resp =="All right" or resp =="yea" or resp =="Yea" or resp =="yeah" or resp =="Yeah" or resp =="indeed" or resp =="Indeed" or resp == "okay" or resp == "Okay" or resp == "ok" or resp =="Ok" or resp == "OK" or resp == "sure" or resp == "Sure":

        questions()

    if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na":
        leave()
        return None

    if resp == "bye" or resp == "Bye":
        leave()
        return None

def questions():
    quest = random.randint(2, 8)
    print("")
    print("Okay, lets talk about this")
    print("")


    if quest ==2:
        print("")
        print("Tell me what happened today?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if quest ==3:
        print("")
        print("What was something good that happened to day?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if quest ==4:
        print("")
        print("What are you grateful for?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if quest ==5:
        print("")
        print("When have you been the most happy?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if quest ==6:
        print("")
        print("What is your idea of the perfect day?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if quest ==7:
        print("")
        print("What is your spirit animal?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if quest ==8:
        print("")
        print("What's your guilty pleasure?")
        print("")
        resp = input(' ')
        resp = resp.lower()
        print("")

    if resp == "bye" or resp == "Bye":
        leave()
        return None

    print("Would you like to talk more?")
    print("")
    resp = input("  ")
    resp = resp.lower()
    print("")

    if resp == "yes" or resp == "Yes" or resp == "sure" or resp =="Sure" or resp =="yup" or resp =="Yup" or resp =="all right"or resp =="All right" or resp =="yea" or resp =="Yea" or resp =="yeah" or resp =="Yeah" or resp =="indeed" or resp =="Indeed" or resp == "okay" or resp == "Okay" or resp == "ok" or resp =="Ok" or resp == "OK" or resp == "sure" or resp == "Sure":

        print("Sweet, let me get another question.")
        print("")
        questions()

    if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na":
        leave()
        return None

    if resp == 'bye' or resp =='Bye':
        leave()
        return None


def posWords(emotion):
    print("")
    if PositiveWord[emotion] <= 3:
        print("Thats cool.")
        print("")
        print("Tell me about it.")
        print("")
        resp = input('  ')
        resp = resp.lower()
        print("")
        if resp == 'bye' or resp =='Bye':
            leave()
            return None
        if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na":
            print("")
            print("You don't have to if you don't want to.")
            print("")
            smallTalk(resp)

        else:
            print("")
            print("That sounds fun.")
            print("")
            smallTalk(resp)
    if PositiveWord[emotion] >=4:
        print("That's great! Tell me more.")
        print("")
        resp= input('    ')
        resp = resp.lower()
        print("")
        if resp == 'bye' or resp =='Bye':
            leave()
            return None
        if resp == 'No' or resp == "no":
            print("")
            print("Thats okay, you don't have to.")
            print("")
            smallTalk(resp)

        elif resp != 'No' or resp != 'no':
            print("That sounds amazing!")
            print("")
            smallTalk(resp)

def negWord(emotion):
    print("")
    if NegativeWord[emotion] >=-3:
        minorNeg(emotion)
    if NegativeWord[emotion] <=-4 and NegativeWord[emotion] >=-6:
        medNeg(emotion)
    if NegativeWord[emotion] >= -7:
        supNeg(emotion)
    if emotion == 'bye' or emotion =='Bye':
        leave()
        return None

def minorNeg(emotion):

    print("I'm sorry to hear that.")
    print("")
    print("What would you have changed about this situation?")
    print("")
    resp = input("  ")
    resp = resp.lower()
    print("")
    if resp == 'bye' or resp =='Bye':
        leave()
        return None
    print("Did you do something you enjoyed today?")
    print("")
    resp = input("  ")
    resp = resp.lower()
    print("")
    if resp == 'bye' or resp =='Bye':
        leave()
        return None
    print("Name a few things that make you happy")
    print("")
    resp = input("  ")
    resp = resp.lower()
    print("")
    if resp == 'bye' or resp =='Bye':
        leave()
        return None
    if resp == "none" or resp == "" or resp == "nothing" or resp == " " or resp ==" " or resp == "i dont know" or resp =="i don't know" or resp== "i dont know." or resp == "i don't know.":
        print("Well if you would like to try something new other people have told use that they have enjoyed things such as cooking, drawing, dancing, singing, puzzles, knitting, and other such things.")
        print("")

    print("Would you like to vent about it?")
    print("")
    resp = input("(Yes or no)  ")
    resp = resp.lower()
    print("")

    if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na":
        smallTalk(emotion)
        return None

    if resp == "yes" or resp == "Yes" or resp == "sure" or resp =="Sure" or resp =="yup" or resp =="Yup" or resp =="all right"or resp =="All right" or resp =="yea" or resp =="Yea" or resp =="yeah" or resp =="Yeah" or resp =="indeed" or resp =="Indeed" or resp == "okay" or resp == "Okay" or resp == "ok" or resp =="Ok" or resp == "OK" or resp == "sure" or resp == "Sure":
        print("Alright, rant away.")
        print("")
        resp == input("    ")
        resp == input("   ")
        print("")
        print("Would You like to talk more?")
        print("")
        resp == input("     ")
        resp = resp.lower()
        print("")
        if resp == "yes" or resp == "Yes" or resp == "sure" or resp =="Sure" or resp =="yup" or resp =="Yup" or resp =="all right"or resp =="All right" or resp =="yea" or resp =="Yea" or resp =="yeah" or resp =="Yeah" or resp =="indeed" or resp =="Indeed" or resp == "okay" or resp == "Okay" or resp == "ok" or resp =="Ok" or resp == "OK" or resp == "sure" or resp == "Sure":
            print("Awesome!")
            print("")
            smallTalk(resp)
            return None
        if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na":
            print("Thats okay I'm sure you have stuff to do.")
            print("")
            leave()
            return None
    return None

def medNeg(emotion):

    print("")
    print("How else would you describe that?")
    print("")
    print("(Please use one word.)")
    print("")
    emotion = input("  ")
    print("")
    if emotion == 'bye' or emotion == 'Bye':
        leave()
        return None
    if NegativeWord[emotion] == -7:
        supNeg(emotion)
        return None


    print("Elaborate on that please.")
    print("")
    emotion = input("  ")
    print("")
    if NegativeWord[emotion] == -7:
        supNeg(emotion)
        return None

    if emotion == 'Bye' or emotion == 'bye':
        leave()
        return None

    print("What other word would you use to describe it?")
    print("")
    emotion = input("  ")
    print("")
    if NegativeWord[emotion] == -7:
        supNeg(emotion)
        return None

    if emotion == 'bye' or emotion == 'Bye':
        leave()
        return None

    print("It's alright to feel "+ emotion +" sometimes just keep in mind that it will get beter just make sure to keep your chin up.")
    return None


def supNeg(emotion):
    if NegativeWord[emotion] == -7:

        print("How long have you felt that way?")
        print("")
        resp = input("Choose one: Days; Weeks; Months; Years  ")
        if resp == "bye" or resp ==" Bye":
            leave()
            return None


        if resp == "Days" or resp == "days" or resp == "Weeks" or resp == "weeks":
            print("")
            print("I hope you know you're capable, brave and significant. Even if you feel like you're not.")

        if resp =="Months" or resp == "months":
            print("")
            print("Give yourself a break. Stop beating yourself up! Everyone makes mistakes,")
            print("has setbacks and failures. You don't come with a book on how to get it right all the time.")

        if resp =="Years" or resp == "years":
            print("")
            print("If you have been feeling this way for this long then I am not your solution. Even if you feel its not that big of deal, your emotional health can negatively affect your physical health.")
            print("Please take time to research your local psychiatrist. Even if you feel you don't need it, its always good to be able to express your emotions and get feedback on them.")
        if resp == "bye" or resp ==" Bye":
            leave()
            return None

        return None

def nuetral(emotion):
    if nuetralWord[emotion] == 0:
        print("Would you say you feel more positive, negatively, or nuetral about the situation?")
        resp = input("  ")
        resp = resp.lower()

        if resp == "negatively":
            minorNeg()
            return None

        if resp == "positive":
            posWords()
            return None

        if resp == "nuetral":
            print("")
            print("That's good. would you like to talk?")
            print("")
            resp = input("    ")
            resp = resp.lower()
            print("")
            if resp == "yes" or resp == "Yes" or resp == "sure" or resp =="Sure" or resp =="yup" or resp =="Yup" or resp =="all right"or resp =="All right" or resp =="yea" or resp =="Yea" or resp =="yeah" or resp =="Yeah" or resp =="indeed" or resp =="Indeed" or resp == "okay" or resp == "Okay" or resp == "ok" or resp =="Ok" or resp == "OK" or resp == "sure" or resp == "Sure":
                smallTalk(emotion)
                return None

            if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na" or resp== "bye" or resp == "Bye":
                leave()
                return None

        return None

    if nuetralWord[emotion] == 1:
        print("")
        print("You should try and get more sleep. Though I understand its hard sometimes.")
        print("")
        print("Would you like to talk more?")
        print("")
        resp = input("")
        resp = resp.lower()
        print("")

        if resp == "yes" or resp == "Yes" or resp == "sure" or resp =="Sure" or resp =="yup" or resp =="Yup" or resp =="all right"or resp =="All right" or resp =="yea" or resp =="Yea" or resp =="yeah" or resp =="Yeah" or resp =="indeed" or resp =="Indeed" or resp == "okay" or resp == "Okay" or resp == "ok" or resp =="Ok" or resp == "OK" or resp == "sure" or resp == "Sure":
            smallTalk(emotion)
            return None

        if resp == "no" or resp == "No" or resp== "nope" or resp== "Nope" or resp== "na" or resp== "Na" or resp== "bye" or resp == "Bye":
            leave()
            return None

        return None

    return None

def leave():
    print("Alright then, good bye. Have a nice day!")
    return None

# CODE START
print("")
print("Hi! My name is Micheal!")
print("")
Name = input("Who are you?      ")
print("")

while Name == "Micheal" or Name =="micheal":

    if Name == "Micheal" or Name == "micheal":
        print("Good human, that is not your name, that is my name. Please enter a new name!")
        print("")
        Name = input("  ")
        print("")

while True:


    print("So, " + Name + " how are you feeling today?")
    print("")
    emotion = input("I feel   ")
    print("")
    emotion = str(emotion)
    emotion = emotion.lower()

    if emotion in NegativeWord:
        negWord(emotion)
        break

    if emotion in PositiveWord:
        posWords(emotion)
        break

    if emotion in nuetralWord:
        nuetral(emotion)
        break

    if emotion == "Bye" or emotion == "bye":
        print("Alright then, good bye. Have a nice day!")
        break

    if emotion != "Bye" or emotion != "bye" or emotion not in PositiveWord or emotion not in NegativeWord:
        print("I'm sorry I didn't understand that would you please use a synonym for it?")
        print("")
