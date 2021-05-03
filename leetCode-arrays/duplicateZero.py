def duplicateZero(arr): 
    print(arr)
    i = 0
    while i<len(arr) -1 :
        print(i)
        if(arr[i] == 0):
            # insert zero
            arr.insert(i,0)

            # removing last element to maintain the array len
            arr.pop(-1)
            i += 2
        else:
            i += 1
        print(arr)
        

    print(arr)
a = [1,0,2,3,0,4,5,0]
a = [1,2,3]
duplicateZero(a)


