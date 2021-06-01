def mergeSortedArray(nums1,nums2):
    # i = 0
    counter1 = 0
    counter2 = 0

    while(counter1 < len(nums1)):

        print('counter1 = ',counter1)
        print('counter2 = ',counter2)

        if( nums1[counter1] >= nums2[counter2] ):
            nums1.insert(counter1,nums2[counter2])
            counter1 += 1
            counter2 += 1
            # pop the last element
            nums1.pop(-1)
        else:
            counter1 += 1

        print(nums1)

    print('after sorting ')
    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
mergeSortedArray(nums1,nums2)