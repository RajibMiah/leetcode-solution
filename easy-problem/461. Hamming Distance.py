def hammingDistance(x, y):
    xor = x ^ y

    hd = 0

    while(xor):
        hd += xor % 2
        xor = xor >> 1

    return hd


print(hammingDistance(3, 1))  # output 1
