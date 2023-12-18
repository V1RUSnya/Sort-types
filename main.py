import metod
import random
import time

def test(arr):
    for i in range (len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def input_arr_randomize():
    arr = []
    random.seed()
    for i in range (10**3): # Кол-во элементов
        arr.append(random.randint(1,1000)) #Диапозон
    return arr

sol = metod.Solution()
formats = "-"*100
inputs = input_arr_randomize()

debug_select = None # Дебаг
print(f"{formats}\nМассив: {inputs}\n{formats}\nКаким методом сортировать?\n0) Выход\n1) Пузырьком\n2) Сортировка выбором\n3) Сортировка вставками")
while True:
    if debug_select == None:
        select = int(input())
    else:
        select = debug_select
    start_time = time.time()
    if select == 0:
        break
    elif select == 1:
        result = sol.bubble(inputs)
    elif select == 2:
        result = sol.selection(inputs)
    elif select == 3:
        result = sol.insertion(inputs)

    end_time = time.time()
    execution_time = end_time - start_time # Время

    if test(result) == True:
        print(f"{result}\nВремя: {round(execution_time,5)} секунды")
        inputs = input_arr_randomize()
    else:
        print("Ошибка в работе!")
        if debug_select != None:
            print(f"Информация для отладки: {result}")
        break