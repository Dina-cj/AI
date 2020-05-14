from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import subprocess
import time

bot=ChatBot('test')
trainer=ListTrainer(bot)
conv=open('chat.txt', 'r').readline()
trainer.train(conv)
subprocess.call("color 2",shell=True)
time.sleep(5);
print("\n[*] Hi I am Queen, Your assistan can I help You?");
# name=input("What is your name");
# app=open('application.txt', 'r').readline()
# trainer.train(app)
while True:
    requst=input('\n[+]you: ')
    response=bot.get_response(requst)
    try:
       syswell=subprocess.call(requst)
       print('Queen: ',syswell)
    except:
        print('\n[+]Queen: ', response)

