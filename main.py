
import speech_recognition as sr
from gtts import gTTS
import os
import time
from pydub import AudioSegment
from pydub.playback import play
import os
import raspi
r = sr.Recognizer()

def speak(output):
    tts = gTTS(text=output, lang='tr', slow=False)
    tts.save("merhaba.mp3")
    os.system("merhaba hulya.mp3")


def berkerfunc(input):
    os.system("omxplayer hulya.mp3")


def isimfunc(input):
    speak(f"Memnun oldum {input.lower().split('benim adım')} bende Şengül")

def doldurfunc():
    raspi.work()

def konus_cevapla(data):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        while True:
            r.adjust_for_ambient_noise(source)
            print(r.energy_threshold)
            time.sleep(0.3)
            if r.energy_threshold > 800:
                speak("Burdayım")
                break
        try:
            ses = r.listen(source, timeout=5, phrase_time_limit=5)
            sonuc = r.recognize_google(ses, language='tr-tr')
            print(sonuc)

            for key in data.keys():
                if key.lower() in sonuc.lower():
                    speak(data[key]['voice'])
                    eval(f"{data[key]['func']}(sonuc)")
                    return "OK"
            else:
                speak("Çok güzel bir soru düşünmem lazım.")
        except sr.WaitTimeoutError:
            speak("Dinleme zaman aşımına uğradı")

        except sr.UnknownValueError:
            speak("Ne dediğini anlayamadım")

        except sr.RequestError:
            speak("İnternete bağlanamıyorum")


data = {

    "benim adım": {"voice": "Çok güzel bir isim", "func": "isimfunc"}, "koy": {"voice": "Tabii Hemen Koyuyorum",func:"doldurfunc"}, "Berker e": {"voice": "Tabii", "func": "berkerfunc"}, "adın": {"voice": "benim adım şengül"}, "tanıyor musun": {"voice": "Tam emin olamadım adını söylermisin"},
    "yaşındasın": {"voice": "Yılbaşında buna cevap vermek yaşlandığımı hatırlatıyor"}, "nasılsın": {"voice": "İyiyim ama alkolü biraz fazla kaçırdım sanırım sen nasılsın"}}

while True:
    print(konus_cevapla(data))
