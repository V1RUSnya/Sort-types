class Solution():
    def bubble(self,l1: list)->list:
        a=0
        while a<= len(l1):
            for i in range (len(l1)-1-a):
                if l1[i]>l1[i+1]:
                    temp = l1[i+1]
                    l1[i+1] = l1[i]
                    l1[i] = temp
            a+=1
            print(l1)