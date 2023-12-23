from random import choice

def binarySearch(data, value):
  high = len(data) - 1
  low = 0
  mid = int((high + low) / 2)
  foundIndex = -1
  while low <= high:
    
    if data[mid] == value:
      #This is done to return the first instance of the target value in the list
      if foundIndex > mid or foundIndex == -1:
        foundIndex = mid

    if data[mid] >= value:
      high = mid -1
      mid = int((high + low) / 2)
      
    else:
      low = mid + 1
      mid = int((high + low) / 2)

  return foundIndex


demo_data = [2, 4, 14, 20, 22, 25, 30, 35, 50, 51, 53, 54, 58, 72, 73, 74, 82, 83, 87, 91]
demo_value = choice(demo_data)

print(f"Searching for {demo_value}")
print(f"Found {demo_value} at index {binarySearch(demo_data, demo_value)}")  