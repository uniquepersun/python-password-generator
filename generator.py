import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()_-=[]}{'.,?><"

all = lower + upper + upper + symbol + number + lower + number + symbol
length = 12
password = "".join(random.sample(all,length))
print("The Password generated for you is :- ",password)

input("Press Enter to exit...")
