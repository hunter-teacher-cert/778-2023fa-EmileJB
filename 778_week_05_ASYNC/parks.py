from sodapy import Socrata
client = Socrata("data.ny.gov", None)

county = input("Enter a county: ")
filter = f"county = '{county}' and year = 2022"

results = client.get("8f3n-xj78", limit=2000, where=filter)

if len(results) == 0:
  print("No such county available")
else:
  counter = 0
  for park in results:
    print(f"{counter}: {park['facility']}")
    counter += 1
  get_attendance = int(input("Enter the number of the park you want to view the attendance of: "))
  print(results[get_attendance]['attendance'])