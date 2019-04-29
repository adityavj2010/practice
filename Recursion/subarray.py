def printSubsequences(arr, index, subarr):
    if len(subarr)>=2:
        if arr.index(subarr[-1])-1!=arr.index(subarr[-2]):
                return
    if index == len(arr):
        if len(subarr) != 0:
            print(subarr)
    else:
        printSubsequences(arr, index + 1, subarr+[arr[index]])
        printSubsequences(arr, index + 1, subarr)

arr = [1, 2, 3, 4, 5]
printSubsequences(arr, 0, [])
