import time

days = int(time.time() // (24 * 60 * 60))
hours = (int((time.time() % (24 * 60 * 60)) // (60 * 60)) - 5) % 12 # Setting time to EST and Non-Military Time
minutes = int(((time.time() % (24 * 60 * 60)) % (60 * 60)) // 60)
seconds = int((((time.time() % (24 * 60 * 60)) % (60 * 60)) % 60))

print(f"{days} days since the epoch")
print(f"Current Time: {hours}:{minutes}:{seconds}")