import pyttsx3 
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import random
import smtplib
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio): 
    '''speaks the given string'''
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''to greet the user at the begining of the program'''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Steve, sir. Please tell me how may I assist you?")

def takeCommand():
    '''it takes microphone input from the user and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1  #1 second of non-speaking audio before a phase is considered complete 
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please, say that again...")
        return "None"
    return query

def sendEmail(to,content):
    '''sending email '''
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('add_your_email_addresss',"your-password")
    server.sendmail('add_your_email_addresss',to,content)
    server.close()

def search_on_google(query):
    '''search for a said query on google search engine'''
    if query:
        print("googling...")
        speak("Googling...")
        query = query.replace(' ', '+')
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        print(f"Searching Google for: {query}")
    else:
        print("No query detected.")

def search_on_youTube(query):
    '''search for a said query on youtube'''
    if query:
        print("Seaching youtube...")
        speak("Searching youtube...")
        query = query.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        print(f"Searching Youtube for: {query}")
    else:
        print("No query detected.")

if __name__=="__main__":
    wishme()
    while True: #program will run until user say 'Exit'
    #if 1:      #program runs for a query, uncomment to use and comment while true
        query=takeCommand().lower() #converts the input string into lowercase

        #logic for executing tasks based onn query
        if 'wikipedia' in query:
            '''searches wikipedia with a said query'''
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Accoring to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            '''open youtube in the browser'''
            speak("Opening youtube...")
            print("Opening youtube...")
            webbrowser.open('youtube.com')
        
        elif 'search with youtube' in query:
            '''search youtube with a said query'''
            print("Please say your query or 'exit' to quit:")
            speak("Please say your query or 'exit' to quit:")
            youTube_query = takeCommand().lower()
            if youTube_query== "exit":
                break
            else:
                search_on_youTube(youTube_query)

        elif 'open google' in query:
            '''open google in the browser'''
            speak("Opening google...")
            print("Opening google...")
            webbrowser.open("https://www.google.com")
            
        elif query =="search with google":
            '''searches google with a said query'''
            print("Please say your query or 'exit' to quit:")
            speak("Please say your query or 'exit' to quit:")
            google_query = takeCommand().lower()
            if google_query== "exit":
                break
            else:
                 search_on_google(google_query)

        elif 'open spotify' in query: 
            '''open spotify on browser'''
            speak("Opening spotify...")
            print("Opening spotify...")
            webbrowser.open('spotify.com')

        elif 'open stack overflow' in query: 
            '''open stack overflow website on browser'''
            speak("Opening Stack Overflow...")
            print("Opening Stack Overflow...")
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query: 
            '''play random song from the chosen dictionary'''
            music_dir='D:\\new'
            songs=random.choice(os.listdir(music_dir))
            print(songs)
            os.startfile(os.path.join(music_dir,songs))

        elif 'time' in query:
            '''tells you the current time''' 
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query: 
            '''opem Visual Studiocode application'''
            codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio code...")
            print("Opening Visual Studio code...")
            os.startfile(codePath)

        elif 'email to himanshu' in query: 
            '''starts the process of sending email'''
            try:
                speak("What should i say?")
                content=takeCommand()
                to="email_address_you_want_to_send_mail"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, i am not able to send your email!")
        elif 'notepad' in  query: 
            '''opens notepad applicaion'''
            speak("Opening notepad")
            print("Opening Notepad...")
            os.startfile("notepad.exe")
        elif 'calculator' in  query: 
            '''open calculator on your system'''
            speak("Opening calculator")
            print("Opening calculator...")
            os.startfile("calc.exe")

        elif 'quit' in query: 
            '''greet the user and exit the program'''
            speak("Glad could help!.see you next time.")
            quit()
        

        


