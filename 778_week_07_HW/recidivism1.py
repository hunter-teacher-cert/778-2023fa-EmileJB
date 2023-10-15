import espeak
from sodapy import Socrata
import speech_recognition as sr


client = Socrata("data.ny.gov", None)
espeak.init()
speaker = espeak.Espeak()

speaker.say("Say The Name Of A County. Press Enter When You're Ready To Speak. Wait 5 Seconds After Pressing Enter If You'd Prefer To Type.")
input("Say The Name Of A County. Press Enter When You're Ready To Speak. Wait 5 Seconds After Pressing Enter If You'd Prefer To Type.")


r = sr.Recognizer()
with sr.Microphone() as source:
    #print("Say something!")
    audio = r.listen(source,5)

county = ""

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    county = (r.recognize_google(audio)).upper()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    county = input("Enter a county: ")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    county = input("Enter a county: ")

filter = f"county_of_indictment = '{county}'"

results = client.get("y7pw-wrny", where=filter)

if len(results) == 0:
  print("No such county available")
else:
  total = 0
  no_returns = 0
  for inmate in results:
    if inmate['return_status'] == "Not Returned":
      no_returns+=1
    total += 1

  print(f"Inmates Not Returned: {no_returns} ({no_returns / total * 100}%)")
  speaker.say(f"Inmates Not Returned: {no_returns} ({no_returns / total * 100}%)")
  input("...pause...")