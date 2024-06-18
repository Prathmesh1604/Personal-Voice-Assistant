import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import keyboard
import pyjokes
import os
from PyDictionary import PyDictionary as Diction
import datetime
from playsound import playsound
from googletrans import Translator
from pywikihow import search_wikihow
import requests 
from bs4 import BeautifulSoup



Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[1].id)


def Speak(audio):

    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    print("  ")
    Assistant.runAndWait()
    

def takecommand(): 

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()
   
def TaskExe():

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            Speak("Good morning")
        elif hour>=12 and hour<18:
            Speak("good afternoon")
    
        else:
            Speak("good evening")

        Speak("I am Jarvis Sir. Please tell me. how may I help You")

    def Music():
        Speak("tell me the name of song")
        musicName = takecommand()

        if 'moonlight' in musicName:
            os.startfile("F:\\music\\Moonlight.mp3")

        elif 'metamorphosis' in musicName:
            os.startfile("F:\\music\\METAMORPHOSIS.mp3")

        else:
            pywhatkit.playonyt(musicName)
        Speak("Your song has been started! , Enjoy")

    def TakeHindi():

        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            command.pause_threshold = 1
            audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"
        
        return query.lower()
                  
    def Tran():
        Speak("tell me the line")
        line = TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak("The Translation For This Line IS :"+Text)
        
    def OpenApps():
        Speak("Ok Sir ")

        if 'code' in query:
            os.startfile("D:\\Microsoft VS Code\\Code.exe")

        elif 'chorme' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'brave' in query:
            os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

        elif 'apple' in query:
            webbrowser.open("https://www.apple.com/in/")

        elif 'maps' in query:
            webbrowser.open("https://www.google.com/maps/place/BMIT+Institute,+Solapur/@17.6673869,75.8044978,18.25z/data=!4m10!1m2!2m1!1sbmit+college!3m6!1s0x3bc5d3815ef6a2ff:0xd10cf5692c676353!8m2!3d17.6670625!4d75.8050625!15sCgxibWl0IGNvbGxlZ2WSAQdjb2xsZWdl4AEA!16s%2Fg%2F11f8hy3rp4?entry=ttu")

        elif 'youtube' in query:
            webbrowser.open("http://www.youtube.com")

        Speak("Your command has been completed")

    def CloseAPPS():
        Speak("ok sir , wait a second")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'chorme' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'brave' in query:
            os.system("TASKKILL /F /im brave.exe")

        Speak("Done!")

    def YoutubeAuto():
        Speak("Whats your Command")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('k')
        
        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'mute' in comm:
            keyboard.press('m')
        
        elif 'skip 10 seconds' in comm:
            keyboard.press('l')

        elif "off full screen" in comm:
            keyboard.press("f")

        elif "play" in comm:
            keyboard.press('k')

        Speak("Done sir!")

    def Dict():
        Speak("Activated Dictionary!")
        Speak("Ask me whatever!")
        probl = takecommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of")
            probl = probl.replace("meaning of","")
            result = Diction.meaning(probl)
            Speak(f"The Meaning For {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of")
            probl = probl.replace("synonym of","")
            result = Diction.meaning(probl)
            Speak(f"The synonym For {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the","")
            probl = probl.replace("jarvis","")
            probl = probl.replace("of")
            probl = probl.replace("antonym of","")
            result = Diction.meaning(probl)
            Speak(f"The antonym For {probl} is {result}")

        Speak("Exited Dictionary!")

    def Temp():
        search = 'temperture in solapur'
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperture = data.find("div",class_= "BNeawe").text
        Speak(f"The temperture outside is {temperture} ")

    
    
    wishMe()
    while True:
       
        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I am JARVIS")
            Speak("Your Personal AI Assistant")
            Speak("How May I Help You")

        elif 'how are you' in query:
            Speak ("I am fine sir!")
            Speak("Whats About You")

        elif 'bye' in query:
            Speak('Ok bye , Sir')

        elif 'search on youtube' in query:
            Speak("Ok sir , this is what i found for our Search")
            query = query.replace("jarvis","")
            query = query.replace("search on youtube","")
            web = "https://www.youtube.com/results?search_query=" +query
            webbrowser.open(web)
            Speak("Done")
        
        elif 'google search' in query:
            Speak("Ok sir , this is what i found for our Search")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done")

        elif 'website' in query:
            Speak("Ok sir , Launching...")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = "https://www."+ web1 + '.com'
            webbrowser.open(web2)
            Speak("Done")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia...")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            kk = pyautogui.screenshot()
            kk.save('F:\\Ss')

        elif 'open brave' in query:
            OpenApps()
        
        elif 'open chrome' in query:
            OpenApps()

        elif ' open youtube' in query:
            OpenApps()

        elif 'open apple website' in query:
            OpenApps()
        
        elif 'open maps' in query:
            OpenApps()

        elif 'open vs code' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close brave' in query:
            CloseAPPS()
        
        elif 'close youtube' in query:
            CloseAPPS()

        elif 'close vs code' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('k')
        
        elif 'full screen' in query:
            keyboard.press('f')

        elif 'mute' in query:
            keyboard.press('m')
        
        elif "off full screen" in query:
            keyboard.press("f")

        elif 'skip 10 seconds' in query:
            keyboard.press('l')

        elif 'youtube tools' in query:
            YoutubeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            Speak("Enter time !")
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake Up")
                    playsound("iron.mp3")
                    Speak("Alarm closed!")

                elif now>time:
                    break

        elif 'translater' in query:
            Speak("Translator activated")
            Tran()

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You tell me to remind you that : " +remeberMsg)
            remember = open('data.txt','w')
            remember.write(remeberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('data.txt','r')
            Speak("You tell me that : " + remember.read())

        elif 'how to' in query:
            Speak("Getting Data From Yhe Internet")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'shut down' in query:
            Speak("Ok sir , System shutting down....")
            break

        elif 'who is your master' in query:
            Speak("me created by team BMIT")

        elif 'temp' in query:
            Temp()
            
            
        
TaskExe()
