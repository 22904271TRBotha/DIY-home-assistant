import speech_recognition as sr

r = sr.Recognizer()
first = 1

with sr.Microphone() as mic:

    print("What can I do for you, Mr. Stark?")
    inputAudio = r.listen(mic)
    while(first):

        try:
            text = r.recognize_google(inputAudio)
            print("You said : {}".format(text))
            first = 0
        except:
            print("pardon?")
    while(1):
        print("Anything else?")
        inputAudio = r.listen(mic)

        try:
            text = r.recognize_google(inputAudio)
            print("You said : {}".format(text))

            if text == "no thanks":
                print("Very well.")
                break
        except:
            print("pardon?")