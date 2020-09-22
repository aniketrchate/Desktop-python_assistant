import pyttsx3 
import PyPDF2
import datetime
import speech_recognition as sr
import pyautogui
import random
import os
import win32api, win32con, win32gui
import wolframalpha
import webbrowser
# -- login insta--
from id_pass import uname_mail,pwd
from instalogin import Insta_login

engine = pyttsx3.init()
wolframalpha_id ='add your id'
engine.runAndWait()
 # -- speak function --  
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
# -- time & date function for taking current time & date --
def time():
  time = datetime.datetime.now().strftime("%I:%M:%S")
  speak(time)

def date():
  year = int(datetime.datetime.now().year)
  month = int(datetime.datetime.now().month)
  date = int(datetime.datetime.now().day)
  speak("Todays date is ")
  speak(date)
  speak(month)
  speak(year)

# -- hello / greeting function for wish you good morning/afternoon/evening by current timing --
def starting():
  hour =datetime.datetime.now().hour
  if hour >= 6 and hour<=12:
    speak("good morning")
  elif hour >= 12 and hour <= 18:
    speak("good afternoon")
  elif hour >= 18 and hour <= 24:
    speak("good evening")
  else:
    speak("its late night !")
  speak("welcome back")    
  speak("what can I do for you ?")
 
# -- takecommand function receive voice from user to do activities defined in main --
def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("taking voice from user")
    r.pause_threshold= 1
    audio = r.listen(source)
  try:
    print("Recognizing...")
    query =r.recognize_google(audio, language='en-US')
    print(query)  
  except Exception as e:
    print(e)
    speak("cant understand please speak again")

    return "None"
  return query  

# -- the sshot is used to screenshot --
def sshot():
  d= pyautogui.screenshot()
  d.save('loc.jpg')

# -- by this we can change desktop background --
def change_bgdesk(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)  


# -- this function read pdf documents --
def pdffile_txt(filename):
    pdfobj=open(filename,'rb')
    pdfread =PyPDF2.PdfFileReader(pdfobj)
    mytext=""
    for pageNum in range(pdfread.numPages):
        pageobj=pdfread.getPage(pageNum)
        mytext += pageobj.extractText()
    pdfobj.close()
    return mytext
def speak_pdffile_txt(text):
    engine= pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()



# <---- MAIN ---->    

if __name__ == "__main__":

  starting()

  while True:
    query =takecommand()
    print(query)

    if"time" in query:
      time()
    elif"date" in query:
      date()

    elif"remember it" in query:
      speak("what should I remember ?")
      data =takecommand()
      speak("you said me to remember " + data)
      remember= open("rem.txt", "w")
      remember.write(data)
      remember.close  

    elif"do you know anything" in query:
      remember =open("rem.txt", "r")
      speak("you said me to remember" + remember.read()) 
    
    elif"sreenshot" in query:
      sshot()
      speak("screenshot has been taken")

    elif "calculate" in query:
      client = wolframalpha.Client(wolframalpha_id)
      indx=query.lower().split().index('calculate')
      query = query.split()[indx + 1:]
      res=client.query(''.join(query))
      ans=next(res.results).text  
      speak(ans)
    
    elif "login Instagram" in query:
      Insta_login(uname_mail,pwd)


    elif"search" in query:
      speak("what do you want to search ?")
      search = takecommand().lower()
      webbrowser.open_new_tab("https://www.google.com/search?q="+search)

    elif "change wallpaper" in query:
      imgpath = r'C://Users/Public/Pictures/Sample Pictures'
      imgs=os.listdir(imgpath)
      img=random.choice(imgs)
      imgsel_rand= imgpath+ "/" +img
      change_bgdesk(imgsel_rand)  

    elif"play songs/videos" in query:
        print("playing")
        dirsong=""
        lisongs=os.listdir(dirsong)
        os.startfile(os.path.join(dirsong,lisongs[1]))
        #you can use random() to play any random song 

    elif"read story" in query:
      text= pdffile_txt("add your location")    
      speak_pdffile_txt(text)  

    elif "close" in query:
      quit()   



