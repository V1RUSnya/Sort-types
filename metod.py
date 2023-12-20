class Solution():
    def bubble(self, arr: list) -> list: # Сортировка пузьрьком
        for j in range (len(arr)-1):
            for i in range(len(arr)-1-j):
                if arr[i] > arr[i+1]:
                    temp = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = temp
        return arr
    
    def selection(self, arr: list) -> list: ## Выбором (Меньше сравнений в сравнении с вставками)
        for j in range (len(arr)-1):
            min = j
            for i in range(1+j, len(arr)):
                if arr[i] < arr[min]:
                    min = i
            temp = arr[j]
            arr[j] = arr[min]
            arr[min] = temp
        return arr
    
    def insertion(self, arr: list) -> list: ## Вставками (Меньше перестановок в сравнении с выбором)
        for i in range (1,len(arr)):
            sort = i-1
            while sort > -1 and arr[sort] > arr[sort + 1]:
                temp = arr[sort]
                arr[sort] = arr[sort + 1]
                arr[sort + 1] = temp
                sort -= 1
        return arr