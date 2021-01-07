# https://leetcode.com/problems/pascals-triangle
def pascalTriangle(n):

    if(n == 0): 
        return []

    i  = 0
    myList = [[1]]
    # using n-1 , because we already starting with first entry i.e. [1]
    while(i < (n-1)):
        k = 0 
        lastEntry = myList[-1]
        newEntry = []
        newEntry.append(1)
        while(k<i):
            newEntry.append(lastEntry[k] + lastEntry[k+1])
            k += 1
        newEntry.append(1)

        myList.append(newEntry)

        i += 1
    return myList

print(pascalTriangle(5))
print(pascalTriangle(0))