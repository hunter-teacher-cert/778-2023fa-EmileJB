from sodapy import Socrata
client = Socrata("data.ny.gov", None)

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

  print(f"Minimum Camps: {security_levels['MINIMUM CAMPS']} ({security_levels['MINIMUM CAMPS'] / total * 100}%)")
  print(f"Minimum Security: {security_levels['MINIMUM SECURITY']} ({security_levels['MINIMUM SECURITY'] / total * 100}%)")
  print(f"Medium Security: {security_levels['MEDIUM SECURITY']} ({security_levels['MEDIUM SECURITY'] / total * 100}%)")
  print(f"Maximum Security: {security_levels['MAXIMUM SECURITY']} ({security_levels['MAXIMUM SECURITY'] / total * 100}%)")
  print(f"Shock Incarceration: {security_levels['SHOCK INCARCERATION']} ({security_levels['SHOCK INCARCERATION'] / total * 100}%)")