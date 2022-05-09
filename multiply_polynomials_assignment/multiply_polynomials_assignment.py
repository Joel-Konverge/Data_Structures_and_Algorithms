def multiply_polynomials(poly1,poly2):
    #storinhg the length of the polynomials in m and n
    m,n=len(poly1),len(poly2)
    #the length of the result list will be sum of length of poly1 and poly2 - 1
    mul=[0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            #each value of poly1 will get multiplied to all the values of poly2 and will be added to the index that gives the sum of the current index of both
            mul[i+j]+=poly1[i]*poly2[j]
    return mul


poly1=[2, 0, 5, 7]
poly2=[3, 4, 2]
# if poly1 or poly2 is empty
if poly1!=[] and poly2 != []:
    print(multiply_polynomials(poly1,poly2))
else:
    print([])