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


filter = f"county_of_indictment = '{county}' and snapshot_year = 2023"

results = client.get("55zc-sp6m", where=filter)

final_string = ""
if len(results) == 0:
  print("No such county available")
else:
  counter = 0
  for inmate in results:
    crime = f"Most Serious Crime: {inmate['most_serious_crime']}"
    print(crime)
    age = f"Current Age: {inmate['current_age']}"
    print(age)
    print()
    final_string += crime + "\n" + age + ".\n\n"
    counter += 1
  
  inmate_number = f"Number of inmates: {counter}"
  print(inmate_number)
  final_string += inmate_number
  speaker.say(final_string)
  input("...pause...")