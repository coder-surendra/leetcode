# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
def intersection(nums1,nums2):

    n = min(len(nums1) , len(nums2))
    i = 0
    nums = []
    while( i < n):

        if(nums1[i] in nums2):
            if(nums1[i] not in nums):
                nums.append(nums1[i])
        i += 1

    # print(nums)
    return nums


def func(nums1,nums2):

    if(len(nums1) < len(nums2)):
        nums = intersection(nums1,nums2)
    else:
        nums = intersection(nums2,nums1)
    # print('inside func')
    return nums

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1 = [1,1]
nums2 = [1,2]

print(func(nums1,nums2))