def palindrom():
    count = 0
    count_1 = 0
    count_2 = -1
    string = input()
    for i in range(len(string) // 2):
        if string[count_1] == string[count_2]:
            count += 1
        count_1 += 1
        count_2 -= 1
    if count == len(string) // 2:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    palindrom()
