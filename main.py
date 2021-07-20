import os


def genList():
    list = []
    for i in range(101):
        list.append(i)
    return list


def guess(lis, left, right, counter):
    os.system('clear')
    if right >= left:
        counter += 1
        mid = (right + left) // 2
        u = input("Is your number " + str(
            lis[mid]) + "\n1. YES!\n2. My number is lower\n3. My number is higher\n4. Exit\nType 1/2/3/4: ")
        if u == "1":
            print("YAAAY! It took me " + str(counter) + " try/tries to guess the number!")
        if u == "2":
            guess(lis, left, mid - 1, counter)
        if u == "3":
            guess(lis, mid + 1, right, counter)
        if u == "4":
            print("BYE BYE!")
    else:
        input("Something went wrong! Let's try again! Press ENTER to continue!")
        guess(lis, 0, len(lis) - 1, 0)


if __name__ == '__main__':
    arr = genList()
    print("Hi! I will guess the number you are thinking of!")
    print(arr)
    guess(arr, 0, len(arr) - 1, 0)
