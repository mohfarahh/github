def findMaxOfArray(array):
    max =  array[0]
    for i in range(len(array)-1):
        if array[i] > max:
            max = array[i]
            
    return max


def findMinOfArray(array):
    min = array[0]
    for i in range(len(array)-1):
        if array[i] < min:
            min = array[i]
            
    return min
# ehatre rgrjkgbdsjgbrjgbsrk bvsw


print(findMaxOfArray([1,2,3,4,5,6]))
print(findMinOfArray([1,2,3,4,5,6]))