

def fizzbuzz(num):
    res_list = ["1", "2"]
    for i in range(3, num+1):
        if i % 3 == 0 and i % 5 == 0:
            res_list.append("FizzBuzz")
        if i % 3 == 0:
            res_list.append("Fizz")
        elif i % 5 == 0:
            res_list.append("Buzz")
        else:
            res_list.append(str(i))
    return res_list


print(fizzbuzz(15))
