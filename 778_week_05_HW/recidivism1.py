from sodapy import Socrata
client = Socrata("data.ny.gov", None)

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