"""
__author__ = 'ozcan dikmen'
datetime= 01.10.19
time(%h.%m)= 18.32
""" 
from random import randint
from time import ctime
import time,os,sys,pyttsx3
from gtts import gTTS
import speech_recognition as sr
from time import ctime
from gtts import gTTS
import PyQt5.QtCore as coremodule
import PyQt5.QtMultimedia as multimedia
#import RPi.GPIO as GPIO
class carol:
    def __init__(self):
        self.app = coremodule.QCoreApplication(sys.argv)
    def cal(self, audioPath):
        url = coremodule.QUrl.fromLocalFile(audioPath)
        content = multimedia.QMediaContent(url)
        player = multimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        player.stateChanged.connect(self.app.quit)
        self.app.exec()
    def gelenses(self, audioString):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 135)
        engine.say(text=audioString)    
        engine.runAndWait()
        engine.stop()
    def dinleme(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
        data=""
        try:
            data=r.recognize_google(audio, language='tr-tr')#dil lang
            data=data.lower()
            print("Kelime: " + data)
        except sr.UnknownValueError:
            print("Söylediğini anlayamadım tekrar söyler misin")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return data
#gelen ses
halhatirsorusu=["nasılsın","naber","ne haber","nasıl gidiyor","naber","keyfin nasıl","keyfin yerinde mi","naber lan","ne haber lan"]
napiyorsunsorusu=["nabıyon","ne yapıyorsun","ne yaparsın","napıyorsun","napıyon","napaysın"]
yaraticisorusu=["mucidin kim","mucidi kim","senin mucidi kim","senin mucidin kim","seni kim yarattı","kim tarafından yaratıldın","yaratıcın kim","seni kim tasarladı","seni kim üretti","kim tarafından üretildin","kim üretti"]
iltifat=["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","çok","iyi","çok iyi"]
saat=["saat","saat kaç","kaç saat"]
gun=["bugün günlerden ne","günler","günlerden","haftanın hangi günü"]
onsolcamac=["ön sol camı aç"]
onsolcamac=["ön sol camı kapa"]
hey=["hey carol","hey kerıl","lan kerıl","lan carol","kerıl orada mısın","kerıl burada mısın","carol burada mısın","carol orada mısın","hey","orada mısın","oradamısın","burada mısın","buradamısın","carol","kerıl","yapay zeka","hey carol orada mısın","hey carol oradamısın","hey carol burada mısın","hey carol buradamısın","hey kerıl orada mısın","hey kerıl oradamısın","hey kerıl burada mısın","hey kerıl buradamısın"]
yapayzekasorusu=["sen yapay zeka mısın","sen yapay zekamısın","carol sen yapay zeka mısın","carol sen yapay zekamısın","kerıl sen yapay zeka mısın","kerıl sen yapay zekamısın"]
#giden ses
halhatirsorusucevap = ["iyiyim sen","çok iyiyim","biraz keyifsizim"]
napiyorsuncevap=["hiç takılıyorum","kop kop canım takılmaca","seninle ilgileniyorum"]
iltifatcevap = ["çok teşekkürler","beni utandırıyorsun","utandım","teşekkürler","yardımcı olabildiysem ne mutlu bana"]
yaraticisorusucevap=["1 ekim 2019 da yaratıldım mucidim Özcan Dikmen tarafından","beni Özcan Dikmen tasarladı","beni Özcan Dikmen üretti"]
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
def konus():
    carol().gelenses("ben kerın senin için ne yapabilirim? Bana bir şeyler söyle")    
def yaratici():
    carol().cal("algila.mp3")
    carol().gelenses(yaraticisorusucevap[randint(0, 2)])  
def halhatir():
    carol().cal("algila.mp3")
    carol().gelenses(halhatirsorusucevap[randint(0, 2)])     
def iltifats():
    carol().cal("algila.mp3")
    carol().gelenses(iltifatcevap[randint(0, 4)])
def saats():
    carol().cal("algila.mp3")
    carol().gelenses("saat şu an"+time.strftime("%H %M "))
def guns():
    a=time.strftime("%A")    
    if a=="Monday":
        a="pazartesi"
    if a=="Tuesday":
        a="salı"
    if a=="Wednesday":
        a="çarşamba"                
    if a=="Thursday":
        a="perşembe"
    if a=="Friday":
        a="cuma"
    if a=="Saturday":
        a="cumartesi"      
    if a=="Sunday":
        a="pazar"
    carol().cal("algila.mp3")        
    carol().gelenses("bugün günlerden "+a)
def heys():
    carol().cal("algila.mp3")
    carol().gelenses("efendim Patron")
def yapayzeka():
    carol().cal("algila.mp3")
    carol().gelenses("evet tamamiyle yapay zekayım ve efendim Özcan Dikmen tarafından 1 ekim 2019 da yaratıldım")   
def napiyorsun():
    carol().cal("algila.mp3")
    carol().gelenses(napiyorsuncevap[randint(0, 2)])          
konus()    
while True:
    voicetotext = carol().dinleme()
    if voicetotext in yaraticisorusu:
        yaratici()
    if voicetotext in halhatirsorusu:
        halhatir()
    if voicetotext in iltifat:
        iltifats()
    if voicetotext in saat:
        saats()
    if voicetotext in gun:
        guns()
    if voicetotext in hey:
        heys()
    if voicetotext in yapayzekasorusu:
        yapayzeka()   
    if voicetotext in napiyorsunsorusu:
        napiyorsun()           
"""        
    if voicetotext in onsolcamac:
        carol().gelenses("peki efendim")        
        GPIO.output(11,True)
    if voicetotext in onsolcamkapa:
        mediamodule.gelenses("peki efendim")        
        GPIO.output(11,False)""" 
        
#kapatma=break        
        