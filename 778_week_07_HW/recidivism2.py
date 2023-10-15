import espeak
from sodapy import Socrata
import speech_recognition as sr


client = Socrata("data.ny.gov", None)
espeak.init()
speaker = espeak.Espeak()

speaker.say("Say A Maximum Age. Press Enter When You're Ready To Speak. Wait 5 Seconds After Pressing Enter If You'd Prefer To Type.")
input("Say A Maximum Age. Press Enter When You're Ready To Speak. Wait 5 Seconds After Pressing Enter If You'd Prefer To Type.")

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
    age = int(input("Enter a maximum age: "))
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    age = int(input("Enter a maximum age: "))

filter = f"age_at_release <= '{age}'"

results = client.get("y7pw-wrny", where=filter)

if len(results) == 0:
  print("No such county available")
else:
  print(len(results))
  total = 0
  parole_violations = 0
  new_offenses = 0
  for inmate in results:
    if inmate['return_status'] == "Returned Parole Violation":
      parole_violations+=1
    elif inmate['return_status'] == "New Felony Offense":
      new_offenses+=1
    total += 1

  speaker.say(f"Inmates Who Violated Paroles: {parole_violations} ({parole_violations / total * 100}%). Press Enter For More Data")
  input(f"Inmates Who Violated Paroles: {parole_violations} ({parole_violations / total * 100}%). Press Enter For More Data")
  speaker.say(f"Inmates With New Offenses: {new_offenses} ({new_offenses / total * 100}%). Press Enter To Quit The Program")
  input(f"Inmates With New Offenses: {new_offenses} ({new_offenses / total * 100}%). Press Enter To Quit The Program")