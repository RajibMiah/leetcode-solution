
def printBinary(num):

    for i in reversed(range(10)):
        print(((num >> i) & 1), end="")

    print(end='\n')


def Main(n):

    # for i in range(8):
    #     printBinary(i)
    #     if (i & 1):
    #         print('odd')
    #     else:
    #         print('even')

    ## divide and multiplication
    # print(n >> 1)
    # print(n << 1)

    # ascii upper and lower case
    # ascii uppercase value 65 - 91 and lowercase value is 97-123

    for i in range(65, 68):
        printBinary(i)
        print(chr(i | 1 << 5))

    for i in range(97, 100):
        printBinary(i)
        print(chr(i & (~(1 << 5))))
    # printend " " space
    print(chr(1 << 5))
    printBinary(ord(" "))
    printBinary(ord('_'))


if __name__ == "__main__":
    Main(5)
