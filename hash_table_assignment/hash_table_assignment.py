def get_index(datalist,key):
    tot=0
    #loop through the letters of key and add the ASCII numbers to result
    for k in key:
        tot+=ord(k)
    #get the remainder using the modulo operator on the total and the length of datalist
    result=tot%len(datalist)
    return result

def get_valid_index(datalist,key): 
    #assigning the result returned from get_index to variable i
    i=get_index(datalist,key)
    while True:
        # if the index has no key and is None then return the index
        if datalist[i] is None:
            return i
        # assigning the key of the index of datalist to k and returning index if k is equal to the key
        k,_=datalist[i]
        if k==key:
            return i
        i+=1    
        # moving i to the start if i is at the last index of the list
        if i==len(datalist):
            i=0


class HashTable:
    def __init__(self,max_size):
        # assigning the max size of the list with all None values to datalist
        self.datalist=[None]*max_size
    def insert(self,key,value):
        #first get the valid index and after getting the index store the key and value on that index in the datalist
        self.datalist[get_valid_index(self.datalist,key)]=(key,value)          
    def find(self,key):
        #get the valid index of the key whose value needs to be returned
        _,value = self.datalist[get_valid_index(self.datalist,key)]
        return value
    def update(self, key, value):
        #update the value of the key 
        self.datalist[get_valid_index(self.datalist,key)]=(key,value)      
    def list_all(self):
        #list all the keys in a form of a list that are not None
        return [k[0] for k in self.datalist if k is not None]


#create an object and pass an arguement for the max size
ht=HashTable(4096)
ht.insert('silent','200')
ht.insert('listen','903')
ht.update('silent','412')
print(ht.find('listen'))
print(ht.list_all())
