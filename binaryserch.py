def binary_search(list, element):

    middle = 0
    start = 0
    end = len(list)
    step = 0

    while(start<=end):
        print("step", step, ":", str(list[start:end+1]))

        step = step + 1
        midlle = (start + end) // 2

        if element == list[middle]:
            return middle

        if element < list[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return - 1


mulist = [1, 2, 3, 4 , 5, 6, 7, 8, 9 ]
target = 2

binary_search(mulist, target)

