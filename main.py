import metod
import random
import time

def test(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
        return True

def input_arr_randomize():
    arr = []
    random.seed()
    for i in range (10**2): #Колво элементов
        arr.append(random.randint(1,100)) #Диапозон
    return arr


sol = metod.Solution()
formats = "-"*100
inputs = input_arr_randomize()

print(f"{formats}\nМассив: {inputs}\n{formats}\nКаким методом сортировать?\n0) Выход\n1) Пузырьком\n2) Сортировка выбором")
while True:
    select = int(input())
    # select = 2 # Debug
    start_time = time.time()
    if select == 0:
        break
    elif select == 1:
        result = sol.bubble(inputs)
    elif select == 2:
        result = sol.Sort_viborom(inputs)
    end_time = time.time()
    execution_time = end_time - start_time
    if test(result):
        print(f"{result}\nВремя: {round(execution_time,5)} секунды")
        inputs = input_arr_randomize()
    else:
        print("Ошибка в работе!")
        break