#Binary search
#As opposed to linear search it assigns a left and right value to a sorted array, halves it, and assigns a middle value, then checks if the mid value is the searched value
# if so => search successful
# if not => whether the searched value is bigger or smaller than the mid value, it changes the position of the left/right anchors, and start iteration again

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sv = 21

def binarysearch(numlist,searchValue):
    numlist.sort()
    left = 0
    right = len(numlist) -1
    while left <= right:
        mid = round((left+right)/2)
        if numlist[mid] == searchValue:
            return str(searchValue)+" found"
        elif numlist[mid] > searchValue:
            right = mid-1
        else:
            left = mid+1
    return "Value not found"

print(binarysearch(nums,sv))
