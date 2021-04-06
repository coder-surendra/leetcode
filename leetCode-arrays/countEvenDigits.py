print("Hello world")

nums = [12,345,2,6,7896]
count = 0
for i in nums:
    if( len(str(i))%2 ==0 ):
        print(str(i) + ' is even')
        count += 1
    else :
        print(str(i) + ' is odd')

print('count = ',count)