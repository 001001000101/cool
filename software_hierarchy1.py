# 底层组件：生成数字列表
def number_generator():
    return [1, 2, 3, 4, 5]

# 上层组件：计算数字列表的平均值
def average_calculator(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

# 主程序
numbers = number_generator()
average = average_calculator(numbers)
print(f"The average is {average}")