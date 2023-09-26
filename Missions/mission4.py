# 题目要求：编写一个函数，接受一个列表作为参数，返回列表中的最大元素。

def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [12, 45, 67, 34, 99, 23]
result = find_max(numbers)
print("最大的数字是：")
print(result)

# 练习：编写一个函数，接受一个列表和一个整数 n 作为参数，返回列表中前 n 个最大的元素。