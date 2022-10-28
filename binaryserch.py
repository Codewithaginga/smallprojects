pos = -1

def search(list, n):

    l_bound = 0
    u_bound = len(list) - 1

    while l_bound <=  u_bound:

        mid = (l_bound + u_bound) // 2

        if list[mid] == n:
            globals() ['pos'] = mid
            return True

        else:
            if list[mid] < n:

                l_bound = mid

            else:

                u_bound = mid


list = [4, 7, 8, 12, 45, 99]

n = 45

if search(list, n):
    print('Found at', pos + 1)

else:
    print('Not found')