from sodapy import Socrata
client = Socrata("data.ny.gov", None)

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

  print(f"Inmates Who Violated Paroles: {parole_violations} ({parole_violations / total * 100}%)")
  print(f"Inmates With New Offenses: {new_offenses} ({new_offenses / total * 100}%)")