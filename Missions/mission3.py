# 题目要求：编写一个函数，接受一个整数 n 作为参数，返回斐波那契数列的前 n 个数字。

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

n = 5
result = fibonacci(n)
print(f"前 {n} 个斐波那契数列数字：")
print(result)

# 练习：编写一个函数，接受一个整数 n 作为参数，返回 n 前的所有质数。