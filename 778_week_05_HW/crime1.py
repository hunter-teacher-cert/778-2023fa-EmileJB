from sodapy import Socrata
client = Socrata("data.ny.gov", None)

county = input("Enter a county: ")
filter = f"county_of_indictment = '{county}' and snapshot_year = 2023"

results = client.get("55zc-sp6m", where=filter)

if len(results) == 0:
  print("No such county available")
else:
  counter = 0
  for inmate in results:
    print(f"Most Serious Crime: {inmate['most_serious_crime']}")
    print(f"Current Age: {inmate['current_age']}")
    print()
    counter += 1
  
  print(f"Number of inmates: {counter}")