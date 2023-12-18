class Solution():
    def bubble(self, arr: list) -> list:
        a = 0
        while a < len(arr):
            for i in range(len(arr)-1-a):
                if arr[i] > arr[i+1]:
                    temp = arr[i+1]
                    arr[i+1] = arr[i]
                    arr[i] = temp
            a += 1
        return arr
    
    def selection(self, arr: list) -> list:
        a = 0
        while a <= len(arr)-1:
            min = a
            for i in range(1+a, len(arr)):
                if arr[i] < arr[min]:
                    min = i
            temp = arr[a]
            arr[a] = arr[min]
            arr[min] = temp
            a += 1
        return arr
    
    def insertion(self, arr: list) -> list:
        for i in range (1,len(arr)):
            sort = i-1
            while sort > -1 and arr[sort] > arr[sort + 1]:
                temp = arr[sort]
                arr[sort] = arr[sort + 1]
                arr[sort + 1] = temp
                sort -= 1
        return arr