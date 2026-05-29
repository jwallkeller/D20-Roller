import random

d20 = int(input("How many d20s? "))

sum = 0

for x in range(0, d20):
  roll = random.randint(1, 20)
  print("Roll #" + str(x + 1) + ": " + str(roll))
  sum += roll
  
avg = sum / d20
print("The average of your roll(s): %.1f" % avg)
