# By：仰晨
# 文件名：py明确类型
# 时 间：2023/5/29 3:09

from typing import List

i: int = 1

i = "aaa11"

print(i)


def greeting(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."


def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)


name = "Alice"
age = 30
print(greeting(name, age))

numbers = [1, 2, 3, 4, 5]
print(sum_numbers(numbers))
