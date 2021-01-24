import random
import speech_recognition as sr
import time


r = sr.Recognizer()
print("Welcome to the py game of GUESSING NUMBERS")
def audio_listen():
    with sr.Microphone() as source:
        print("Guess a number number")
        print("Speak.................")
        audio = r.listen(source)
        return audio
    
def catch_audio(audio):
    try:
        q = r.recognize_google(audio)
        print("Random number generated is->>>>>",q)
        return q
    except sr.UnknownValueError:
        print("UnknownValueError")
        pass
    except sr.RequestError:
        print("RequestError")
        pass

ra = str(random.randrange(1,11))
print(ra)
n = audio_listen()
w = catch_audio(n)
count = 0

play_game = 'y'

while play_game == 'y':
    count = count + 1
    if w == ra:
        if count == 1:
            print("You have guessed the corrent number in {}st attempt!!!!!".format(count))
            print("Bye!")
            time.sleep(5)
            quit()
        elif count > 1:
            if count == 3:
                print("You have guessed the correct number in {}rd attempt!".format(count))
                print("Bye!")
                time.sleep(5)
                quit()
            else:
                print("You have guessed the correct number in {}th attempt!".format(count))
                print("Bye!")
                time.sleep(5)
                quit()
    else:
        print("You have guessed the wrong number!!!!!")
        print("Say again")
        n = (audio_listen())
        w = catch_audio(n)