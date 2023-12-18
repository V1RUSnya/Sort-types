import metod
from random import randint

sol = metod.Solution()

input = []
for i in range (10):
    input.append(randint(1,100))

sol.bubble(input)