def countEven(num):
    count = 0

    def isEven(digit):
        digitSum = 0

        while(digit):
            digitSum += digit % 10

            digit //= 10

        return digitSum % 2 == 0

    for i in range(1, num + 1):

        if isEven(i):
            count += 1

    return count


print(countEven(30))  # Output 14
