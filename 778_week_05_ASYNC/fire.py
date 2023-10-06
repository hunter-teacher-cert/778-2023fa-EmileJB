from sodapy import Socrata
client = Socrata("data.ny.gov", None)

city = input("Enter a city: ")
filter = f"city = '{city}'"

results = client.get("qfsu-zcpv", limit=2000, where=filter)

if len(results) == 0:
  print("No such city available")
else:
  print(f"Phone Number: {results[0]['phone_number']}")
  print(f"Google Maps Link: https://maps.google.com/?q={results[0]['lat']},{results[0]['long']}")