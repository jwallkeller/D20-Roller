
### Use this space to try out ideas and free code ###

import random

d20 = int(input("How many d20s?"))

sum = 0

for x in range(1, d20):
  roll = random.randint(1, 20)
  sum += roll
  
avg = sum / d20
  
print("The sum of your roll(s): " + str(sum))
print("The average of your roll(s): %.1f" % avg)
