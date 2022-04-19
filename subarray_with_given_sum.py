def subarray(a,t):
    #using try and expect to handle the error where the list is empty
    try:
        i=0
        l=0
        r=a[0]
        while i<len(a)-1:
            #adding the value of i+1 to r
            r+=a[i+1]
            #checking if r is greater than target if yes then changing the value of r to the current + next element
            if r>t:
                r=a[i]+a[i+1]
                #setting lower value to i
                l=i
            if r==t:
                #if r is equal to t then return the lower and higher value 
                return (l,i+2)
            i+=1
    except:
        return None

a=[1, 7, 4, 2, 1, 3, 11, 5]
t=10
print(subarray(a,t))
