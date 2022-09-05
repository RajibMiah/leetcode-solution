# time complexity O(N)
def reverse(x):
    result = 0
    sign = [1, -1][x < 0]
    while(x != 0):
        reminder = abs(x) % 10
        new_result = result * 10 + reminder
        x = abs(x) // 10
        result = new_result
    return (sign * result) if result.bit_length() < 32 else 0


print(reverse(-123))
print(reverse(120))
print(reverse(-1534236469))  # expected outpu 0
