import metod
from random import randint
import time

sol = metod.Solution()
inputs = []
for i in range (10): #Колво элементов
    inputs.append(randint(1,100)) #Диапозон

print(f"Массив: {inputs}\nКаким методом сортировать?\n0)Выход\n1)Пузырьком\n2)")
while True:
    select = int(input())
    start_time = time.time()
    if select == 0:
        break
    elif select == 1:
        result = sol.bubble(inputs)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{result}\nВремя: {round(execution_time)} секунд")