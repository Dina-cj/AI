from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from playsound import playsound
import subprocess
import time
from gtts import gTTS
import os
# import webbrowser
# import Levenshtein_search

requst=''
response=''
language = 'en'

bot = ChatBot('test')

def triner():
    global bot
    trainer = ListTrainer(bot)
    # conv = open('chat.txt', 'r').readline()
    trainer.train([
                  "how are you?",
                  "Thank you to at all, your computer is safe not virus found!."
                 ])
    time.sleep(5);
    subprocess.call("color 2", shell=True)

    queen_well="Hi an hello every one, I am Queen Your assistan can I help You?"
    print("\n[*]",queen_well);
    queen_well_audio = gTTS(text=str(queen_well), lang=language, slow=False)
    queen_well_audio.save("queen_well_voice.mp3")
    playsound('queen_well_voice.mp3')
    os.remove('queen_well_voice.mp3')
def respect():
    global bot
    global requst
    global response
    while True:
        requst = input('\n[+]you: ')
        response = bot.get_response(requst)
        answer = str(response)
        try:
            subprocess.call(requst)
        except:
            tts = gTTS(text=answer, lang=language, slow=False)
            tts.save('queen_voice.mp3')
            print('\n[+]Queen: ', answer)
            playsound('queen_voice.mp3')
            os.remove('queen_voice.mp3')




triner()
respect()




