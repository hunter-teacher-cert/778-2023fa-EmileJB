import espeak
from sodapy import Socrata
import speech_recognition as sr


client = Socrata("data.ny.gov", None)
espeak.init()
speaker = espeak.Espeak()

speaker.say("Say A Minimum Age. Press Enter When You're Ready To Speak. Wait 5 Seconds After Pressing Enter If You'd Prefer To Type.")
input("Say A Minimum Age. Press Enter When You're Ready To Speak. Wait 5 Seconds After Pressing Enter If You'd Prefer To Type.")


r = sr.Recognizer()
with sr.Microphone() as source:
    #print("Say something!")
    audio = r.listen(source,5)

age = 0

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    age = int(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    age = int(input("Enter a minimum age: "))
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    age = int(input("Enter a minimum age: "))

filter = f"current_age >= '{age}' and snapshot_year = 2023"

results = client.get("55zc-sp6m", where=filter)

if len(results) == 0:
  print("No such range available")
else:
  security_levels = {"MEDIUM SECURITY": 0,
                    "MAXIMUM SECURITY": 0,
                    "MINIMUM SECURITY": 0,
                    "SHOCK INCARCERATION": 0,
                    "MINIMUM CAMPS": 0}
  total = 0
  for inmate in results:
    security_levels[inmate["facility_security_level"]] += 1
    total += 1

  speaker.say(f"Minimum Camps: {security_levels['MINIMUM CAMPS']} ({security_levels['MINIMUM CAMPS'] / total * 100}%). Press Enter For More Data")
  input(f"Minimum Camps: {security_levels['MINIMUM CAMPS']} ({security_levels['MINIMUM CAMPS'] / total * 100}%). Press Enter For More Data")
  speaker.say(f"Minimum Security: {security_levels['MINIMUM SECURITY']} ({security_levels['MINIMUM SECURITY'] / total * 100}%). Press Enter For More Data")
  input(f"Minimum Security: {security_levels['MINIMUM SECURITY']} ({security_levels['MINIMUM SECURITY'] / total * 100}%). Press Enter For More Data")
  speaker.say(f"Medium Security: {security_levels['MEDIUM SECURITY']} ({security_levels['MEDIUM SECURITY'] / total * 100}%). Press Enter For More Data")
  input(f"Medium Security: {security_levels['MEDIUM SECURITY']} ({security_levels['MEDIUM SECURITY'] / total * 100}%). Press Enter For More Data")
  speaker.say(f"Maximum Security: {security_levels['MAXIMUM SECURITY']} ({security_levels['MAXIMUM SECURITY'] / total * 100}%). Press Enter For More Data")
  input(f"Maximum Security: {security_levels['MAXIMUM SECURITY']} ({security_levels['MAXIMUM SECURITY'] / total * 100}%). Press Enter For More Data")
  speaker.say(f"Shock Incarceration: {security_levels['SHOCK INCARCERATION']} ({security_levels['SHOCK INCARCERATION'] / total * 100}%). Press Enter To Quit The Program")
  input(f"Shock Incarceration: {security_levels['SHOCK INCARCERATION']} ({security_levels['SHOCK INCARCERATION'] / total * 100}%). Press Enter To Quit The Program")