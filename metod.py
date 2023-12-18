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
        return l1
    
    def Sort_viborom(self,l1: list)->list:
        min,a = 0,0
        while a <= len(l1)-1:
            for i in range (1+a,len(l1)):
                if l1[i]<l1[min]:
                    min = i
            temp = l1[a]
            l1[a] = l1[min]
            l1[min] = temp
            a+=1
            min = a
        return l1