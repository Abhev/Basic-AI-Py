#imporing modules 

from win32com.client import Dispatch
import speech_recognition as sr
import os
import PIL
import datetime
from googlesearch import search
import wikipedia
import ssl
from tkinter import *

import tkinter as Tkinter
import webbrowser
import datetime
import calendar

from tkinter.ttk import *
from time import * 

#adding basic necessities for big work in AI
engine = Dispatch("SAPI.SpVoice")
now = datetime.datetime.now() #for today's day function
 
#making lists area
friend = ['trishant', 'raghav', 'chayanveer', 'hriday','neelabh','nikhil','tanmay','atharv']; 

#functions are defined below
def countdown(t):
    while t > 0:
        print(t)
        t = t-1
        time.sleep(1)
   
    engine.Speak("Wake up,sir")
    engine.Speak("Tring-tringggggg-tring-trinng")
    engine.Speak("Wake up,sir")
    engine.Speak("Tring-tringggggg-tring-trinng")
    engine.Speak("Wake up,sir")
    engine.Speak("Tring-tringggggg-tring-trinng")
    engine.Speak("Sir,please wake up. Dum-Dama-dum")
    exit()
def findDay(date): 
    finder = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[finder]) 
  
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=4 and hour < 12:

        engine.Speak("Good Morning")
        print("Good Morning")
        engine.Speak("Hello Sir,My name is AI. How can I help u")
        print("Hello Sir,My name is AI. How can I help you")
    elif hour >= 12 and hour < 18 :
                # creating tkinter window 
          
            engine.Speak("Good Afternoon")
            print("Good Afternoon")
            engine.Speak("Hello Sir,My name is AI. How can I help u")
            print("Hello Sir,My name is AI. How can I help you")
        
    elif hour >= 18 and hour < 24:
          
          
  
        
        engine.Speak("Good Evening")
        print("Good Evening")
        engine.Speak("Hello Sir,My name is AI. How can I help u")
        print("Hello Sir,My name is AI. How can I help you")
    else:
        engine.Speak("Hello Sir,my name is AI.How can i help u")
        print("Hello sir, how can I help you")

def author():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.Speak("Listening")
        print("Speak...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            engine.Speak("Recognizing")
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            engine.Speak('Try again,sir')
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
    return query
if __name__ == "__main__" : #this is the main place where our code will run

    wishme() 
    
    while True:   #To make it run always.

        query = author().lower()
        
        if "youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            engine.Speak("Done,sir")
        elif "wikipedia" in query:
            webbrowser.open("https://www.wikipedia.org/")
          
        elif "google" in query:
            webbrowser.open("https://www.google.com/")
            
        elif "bigbasket" in query:
            webbrowser.open("https://www.bigbasket.com/")
            engine.Speak("Done,sir")
        elif "big basket" in query:
            webbrowser.open("https://www.bigbasket.com/")
            engine.Speak("Done,sir")
        elif "edx" in query:
            webbrowser.open("https://www.edx.org/")
            engine.Speak("Done,sir")
        elif "coursera" in query:
            webbrowser.open("https://www.coursera.org/")
            engine.Speak("Done,sir")
        elif "grofers" in query:
            webbrowser.open("https://grofers.com/")
       
            engine.Speak("Done,sir")
        elif "code academy" in query :
           
           webbrowser.open("https://www.codecademy.com/")
           engine.Speak("Done,sir")
        elif "code with harry" in query:
           webbrowser.open("https://www.youtube.com/CodeWithHarry")
           engine.Speak("Done sir")
        elif "current time" in query:
            timecheck = datetime.datetime.now().strftime("%H,%M,%S")
            engine.Speak(f"Sir,the time is{timecheck}")
        elif "who am i" in query:
            engine.Speak("I am not sure who you are but i can assure that you are using MR.Abhi's interface")
        elif "who are you" in query :
            engine.Speak("I am Mr.AI made for simple help in laptops.")
        elif "is better than you" in query :
            engine.Speak("I am not sure about that.But I am sure that all AIs are brothers and sisters ")
            
        elif "i am in which country" in query:
            engine.Speak("I am not sure,but i believe that this interface was made in India")
        elif "do you learn" in query:
            engine.Speak("I always try to learn new things")
        elif "today's day" in query:
            engine.Speak("Finding Day from files")
            print(now.strftime(' %A, %B %dth, %Y'))
            engine.Speak(now.strftime(' %A, %B %dth, %Y'))
        elif "today's date and day" in query:
            engine.Speak("Finding Day and Date from files")
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print(now.strftime(' %A, %B %dth, %Y'))
        elif "today's date" in query:
           engine.Speak("Finding today's date from files")
           print(now.strftime('%Y-%m-%d %H:%M:%S'))
        elif "quit" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 20 and hour < 25 :
                 
          
                engine.Speak("Good Night,Sir")
                print("Good Night")
                
        
            exit()
        elif "exit" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 20 and hour < 25 :
                 
          
                engine.Speak("Good Night,Sir")
                print("Good Night")
                
        
            exit()
            
        elif "off" in query:
            break
        elif "hibernate" in query:
            break
        elif "shut down" in query:
            exit()
        elif "timer" in query:
            engine.Speak("How many seconds long timer, Do you want. Please type here")
            engine.Speak("To off the timer in between or in between voice.Pls enter Ctrl+C twice")
            minutes = input("")
            while not minutes.isdigit():
                engine.Speak("That wasn't an integer.Pls Enter an integer,sir:")
                print("That wasn't an integer.Pls Enter an integer,sir:")
                minutes = input()
            minutes = int(minutes)
            countdown(minutes)

        
        elif "am i audible" in query:
            engine.Speak("Yes sir, you are clearly audible for me")
        elif "can you hear me" in query:
            engine.Speak("Yes sir, you are totally audible to me")
        elif "can u hear me" in query:
            enigne.Speak("Yes sir, you are totally audible to me")
        

       
        elif "sports quiz" in query:
            engine.Speak("Hello sir, I am Sports-ai-quizer.You are welcome to my home. As you have wanted to play Sports quiz,here u go")
            webbrowser.open("https://www.britannica.com/quiz/sports-quiz")

        elif "cricket quiz" in query:
                engine.Speak("Opening Quizzes Book from Britanica for public use")
                webbrowser.open("https://www.britannica.com/quiz/classic-cricket-quiz")
        elif "tennis quiz" in query:
                  engine.Speak("Finding Tennis Quiz from Open-Source Areas,")
                  webbrowser.open("https://www.beano.com/posts/the-ultimate-tennis-quiz")
                  engine.Speak("Done,sir")
        elif "olympics quiz" in query:
                engine.Speak("Finding Quiz from Britanica Books")
                webbrowser.open("https://www.britannica.com/quiz/the-olympic-games")
                engine.Speak("Enjoy sir, Best Of Luck")
        elif "irctc" in query:
            webbrowser.open("https://www.irctc.co.in/nget/train-search")
        elif "calculator" in query:
            webbrowser.open("https://www.online-calculator.com/full-screen-calculator/")
        elif "byju's" in query:
            webbrowser.open("https://learn.byjus.com")
        

        elif "tcs" in query:
            engine.Speak("Processing and Finding Bookmarks")
            webbrowser.open("https://g05.tcsion.com/LX/Dashboard")
            engine.Speak("Done.What other job can i help u with,sir")
        elif "history" in query:
            webbrowser.open("https://g05.tcsion.com/LX/contents/content_home?c_id=vibgyor-high-grade-7-history-ay-20-21-922-3024&content_player=true&my_courses=my_courses")
        elif "geography" in query:
            webbrowser.open('https://g05.tcsion.com/LX/contents/content_home?c_id=vibgyor-high-grade-7-geography-ay-20-21-922-3024&content_player=true&my_courses=my_courses')
        elif "computer" in query:
            webbrowser.open("https://g05.tcsion.com/LX/contents/content_home?c_id=vibgyor-high-grade-7-computer-ay-20-21-922-3024&content_player=true&my_courses=my_courses")
        elif "clock" in query:
            # creating tkinter window 
            engine.Speak("Making a Clock using Tkinter Interface by extracting data from Abhev's Files")
            clock = Tk() 
            clock.title('Clock')
            clock.geometry("600x150")
            clock.minsize(600, 150)
            clock.maxsize(600, 200)
  
            # This function is used to  
            # display time on the label 
            def time(): 
                string = strftime('%H:%M:%S %p') 
                lbl.config(text = string) 
                lbl.after(1000, time) 
            # Styling the label widget so that clock 
            # 
            lbl = Label(clock, font = ('calibri', 80, 'bold'), 
                        background = 'purple', 
                        foreground = 'black') 
  
            # Placing clock at the centre of the window of tkinter
            
            lbl.pack(anchor = 'center') 
            time() 
            mainloop()
        elif "my friends" in query:
                engine.Speak("Okay,sir. Using Files to find your 1/4 th friends of yours")
                engine.Speak(friend[0])
                print(friend[0])
                engine.Speak(friend[1])
                print(friend[1])
                engine.Speak(friend[6])
                print(friend[6])
                engine.Speak(friend[2])
                print(friend[2])
                engine.Speak(friend[3])
                print(friend[3])
                engine.Speak(friend[4])
                print(friend[4])
                engine.Speak(friend[5])
                print(friend[5])


        elif "hahahahaha" in query:
            engine.Speak("I am still getting info related to your question,thus you may try something else till the time.")
        elif "science textbook" in query:
            engine.Speak("Finding File from TCS-ION,May take some time")
            
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Term1_Sci_PCB_Syllabus_Ronak.pdf")
        elif "science text book" in query:
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Term1_Sci_PCB_Syllabus_Ronak.pdf")
        
        elif "maths textbook term one" in query:
            engine.Speak("Finding from TCS-ION")
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Math_TERM_1_HOMENOTES.pdf")
        elif "maths textbook term 1" in query:
            engine.Speak("Finding from TCS-ION")
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Math_TERM_1_HOMENOTES.pdf")
        elif "maths text book term 1" in query:
            engine.Speak("Finding from TCS-ion")
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Math_TERM_1_HOMENOTES.pdf")
        elif "time for lunch" in query:
            webbrowser.open("https://www.dailymail.co.uk/health/article-2593219/Revealed-The-best-times-eat-breakfast-lunch-dinner-want-lose-weight-need-make-sure-youre-7am.html#:~:text=Revealed%3A%20The%20best%20times%20to%20eat%20breakfast%2C%20lunch,in%20the%20evening%2C%20so%20calories%20are%20not%20burned")
       
        elif "india covid tracker" in query:
            webbrowser.open("https://bing.com/covid/local/india")
            engine.Speak("here you go,sir. This is a live Covid Tracker made by Microsoft bing")
        elif "global covid tracker" in query:
            webbrowser.open("https://bing.com/covid")

            engine.Speak("here you go,sir. This is a live Covid Tracker made by Microsoft bing")
        elif "covid19 india" in query:
            engine.Speak("Finding Covid-19 India.org")
            webbrowser.open("https://www.covid19india.org/")
            engine.Speak("Done,sir")
        elif "worldometer coronavirus" in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/")
            engine.Speak("This is a Covid-19 tracker made by worldometer.")

        elif "Covid-19 symptoms" in query:
            engine.speak("Making an Covid-19 Symptoms file")
            webbrowser.open("file:///E:/Abhev/covid-19.html")
            engine.Speak("You can find mainly all of the covid-19 symptoms can be found in this link")
        elif "What is Covid-19" in query:
            engine.Speak('Covid-19(even called Coronavirus) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).[9] It was first identified in December 2019 in Wuhan, Hubei, China, and has resulted in an ongoing pandemic.[10][11] The first confirmed case has been traced back to 17 November 2019 in Hubei.[12] As of 6 August 2020, more than 18.7 million cases have been reported across 188 countries and territories, resulting in more than 706,000 deaths. More than 11.3 million people have recovered.[8] ')
            print('Covid-19(even called Coronavirus) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2).[9] It was first identified in December 2019 in Wuhan, Hubei, China, and has resulted in an ongoing pandemic.[10][11] The first confirmed case has been traced back to 17 November 2019 in Hubei.[12] As of 6 August 2020, more than 18.7 million cases have been reported across 188 countries and territories, resulting in more than 706,000 deaths. More than 11.3 million people have recovered.[8] ')
        elif "grade 7 online timetable" in query:
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Online/Pdf_timetable/TimeTable-PDF.pdf")
            engine.Speak("But sir as i got info from I-Camous-Buddy, you are going to have a different day timetbale on a different day. SO i am Opening That file too.")
            webbrowser.open("file:///E:/Abhev/1@Academics/Class7/Online/@Review1/Grade%207%20-%20VLS%20TT%20AUGUST%202020.pdf")
        
                        
        else:
              engine.Speak("I am not sure with this, but you can try something other with me too")
              #engine.Speak("Please Speak")










             
             