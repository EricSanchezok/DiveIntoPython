# 题目要求：编写一个函数，接受一个字符串作为输入，然后返回该字符串中**单词**顺序颠倒的新字符串。

def reverse_words(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

input_str = "Hello python"
result = reverse_words(input_str)
print("颠倒后的字符串：")
print(result)


# 练习：编写一个函数，接受一个字符串作为输入，返回整体的颠倒字符串。