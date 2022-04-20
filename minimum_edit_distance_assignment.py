def min_dist(str1, str2):
    #if one of the string is empty then return the length of the other 
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1[-1] == str2[-1]:
        #if both the characters are same so we will reduce the index by 1 as the values are same
        return min_dist(str1[:-1], str2[:-1])
    else:
        return 1 + min(
            min_dist(str1, str2[:-1]),#insertion: the value is removed from both but as a new value is added to str1 m is not deducted
            min_dist(str1[:-1], str2),#deletion:  the value is removed from str1         
            min_dist(str1[:-1], str2[:-1])#substitution: the value is replaced with the same letter as str2 and so both are deducted by 1 as the letter are now same

        )
print(min_dist("intention","execution"))