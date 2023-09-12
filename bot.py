import cfile
import pyttsx3
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greet(bot_name, birth_year):
    print("Hello ,My name is ",end="")
    print("\033[94m {}\033[00m".format(bot_name))
    talk("Hello! My name is PYJAC-A tri programming learning bot.")
    print("I was created in", "\033[91m {}\033[00m".format(birth_year))
    talk("I was created in 2021")


def remind_name():
    print("\033[95m{}\033[00m".format('Please, remind me your name.'))
    talk("please, remind your name.")
    name = input("Enter ur name:")
    print("\033[91m{}\033[00m".format('What a great name you have'),"\033[95m {}\033[01m".format(name),"!")
    talk("What a great name you have")
    talk(name)


def guess_age():
    print('okay,Let me guess your age.')
    talk("okay,Let me guess your age.")
    print('Enter remainders of dividing your age by 3, 5 and 7 in each line')
    talk('Enter remainders of dividing your age by 3, 5 and 7 in each line')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0}; that's a good time to start programming!".format(age))
    talk("Your age is {0}; that's a good time to start programming!".format(age))

greet('PYJAC-A tri programming learning bot', '2021')
remind_name()
print("\033[93m{}\033[02m".format("would you like me to guess your age? 'if yes make sure that you are good at finding the remainder!'"))
talk("would you like me to guess your age? 'if yes make sure that you are good at finding the remainder!'")
yor = input()
if(yor == ( "yes" or "Yes" or "YES" or "y" or "Y" or "S" or "s" )):
    guess_age()
else:
    print("it's ok")
    talk("it's ok")
obj=cfile.prog()
obj.program()
