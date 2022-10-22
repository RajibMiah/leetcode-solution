def intToRoman(num):
    result = ""
    num_arr = [1000, 900, 500, 400, 100,  90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC",
             "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    while(num > 0):

        if (num // num_arr[i] > 0):

            val = num // num_arr[i]
            num = num % num_arr[i]

            result += roman[i] * val

        i += 1

    return result


print(intToRoman(1994))  # output "MCMXCIV"
