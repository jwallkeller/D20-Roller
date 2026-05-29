import random

d4 = int(input("How many d4s? "))
d6 = int(input("How many d6s? "))
d8 = int(input("How many d8s? "))
d10 = int(input("How many d10s? "))
d12 = int(input("How many d12s? "))

sum = 0

if d4 > 0:
    print("D4 Results")

for x in range(0, d4):
    roll = random.randint(1, 4)
    print("\tRoll #" + str(x+1) + ": " + str(roll))
    sum += roll

if d6 > 0:
    print("D6 Results")

for x in range(0, d6):
    roll = random.randint(1, 6)
    print("\tRoll #" + str(x+1) + ": " + str(roll))
    sum += roll

if d8 > 0:
    print("D8 Results")

for x in range(0, d8):
    roll = random.randint(1, 8)
    print("\tRoll #" + str(x+1) + ": " + str(roll))
    sum += roll

if d10 > 0:
    print("D10 Results")

for x in range(0, d10):
    roll = random.randint(1, 10)
    print("\tRoll #" + str(x+1) + ": " + str(roll))
    sum += roll

if d12 > 0:
    print("D12 Results")

for x in range(0, d12):
    roll = random.randint(1, 12)
    print("\tRoll #" + str(x+1) + ": " + str(roll))
    sum += roll

print("The sum of your roll(s): " + str(sum))