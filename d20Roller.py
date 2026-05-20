
### Use this space to try out ideas and free code ###

import random

d20 = int(input("How many d20s? "))

sum = 0

for x in range(0, d20):
  roll = random.randint(1, 20)
  print("Roll " + str(x + 1) + ": " + str(roll))
  sum += roll
  print("Running sum: " + str(sum) + "\n")
  
avg = sum / d20
  
print("The sum of your roll(s): " + str(sum))
print("The average of your roll(s): %.1f" % avg)
